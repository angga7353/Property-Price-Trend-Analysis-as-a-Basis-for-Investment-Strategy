from datetime import datetime, timedelta
import pandas as pd
import re
from sqlalchemy import create_engine
from elasticsearch import Elasticsearch, helpers
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator

# Default Arguments
default_args = {
    'owner': 'Angga',
    'start_date': datetime(2024, 11, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG Definition
with DAG(
    dag_id='etl_postgres_to_kibana',
    description='ETL dari PostgreSQL ke Elasticsearch (Kibana)',
    schedule_interval='10,20,30 9 * * 6',
    default_args=default_args,
    catchup=False
) as dag:
    
    # Connection Configs
    # PostgreSQL
    POSTGRES_USER = 'airflow'
    POSTGRES_PASSWORD = 'airflow'
    POSTGRES_HOST = 'postgres'
    POSTGRES_PORT = '5432'
    POSTGRES_DB = 'airflow'
    POSTGRES_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # Elasticsearch
    ES_HOST = "http://elasticsearch:9200"
    ES_INDEX = "kibana"

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    @task()
    def fetch_from_postgresql():
        engine = create_engine(POSTGRES_URL)
        query = "SELECT * FROM table_m3;"
        df = pd.read_sql(query, engine)
        df.to_csv('/opt/airflow/data/P2M3_angga_data_raw.csv', index=False)
        print("Fetched from PostgreSQL")

    @task()
    def data_cleaning():
        df = pd.read_csv('/opt/airflow/data/P2M3_angga_data_raw.csv')

        # Normalisasi nama kolom
        def normalize_column(col):
            col = col.strip()
            col = re.sub(r'[^\w\s]', '', col)
            col = re.sub(r'\s+', '_', col)
            return col.lower()

        df.columns = [normalize_column(col) for col in df.columns]

        # Handling missing values
        df.fillna(df.median(numeric_only=True), inplace=True)
        df.fillna('', inplace=True)

        # Hapus duplikat
        df.drop_duplicates(inplace=True)

        # Tambah kolom ID unik
        df.insert(0, 'id', range(1, len(df) + 1))

        df.to_csv('/opt/airflow/data/P2M3_Angga_data_clean.csv', index=False)
        print("Data cleaned and saved to CSV")

    @task()
    def post_to_elasticsearch():
        es = Elasticsearch(ES_HOST)
        df = pd.read_csv('/opt/airflow/data/P2M3_Angga_data_clean.csv')

        actions = [
            {
                "_index": ES_INDEX,
                "_source": row.dropna().to_dict()
            }
            for _, row in df.iterrows()
        ]

        helpers.bulk(es, actions)
        print(f"Posted to Elasticsearch index '{ES_INDEX}'")

    # Workflow
    start >> fetch_from_postgresql() >> data_cleaning() >> post_to_elasticsearch() >> end

# Judul Project

## Repository Outline
P2-M3/Angga_Fadhlurrahman
|
├── description.md
├── P2M3_Angga_ddl.txt
├── P2M3_Angga_data_raw.csv
├── P2M3_Angga_data_clean.csv
├── P2M3_Angga_DAG.py
├── P2M3_Angga_DAG_graph.jpg
├── P2M3_Angga_conceptual.txt
├── P2M3_Angga_GX.ipynb
├── README.md
├── /images
      ├── introduction & objective.png
      ├── plot & insight 01.png
      ├── plot & insight 02.png
      ├── plot & insight 03.png
      ├── plot & insight 04.png
      ├── plot & insight 05.png
      ├── plot & insight 06.png
      └── kesimpulan.png

## Problem Background
Dalam industri properti, untuk memahami tren harga di berbagai wilayah merupakan kunci utama bagi investor dan perusahaan pengembang dalam menentukan lokasi yang strategis untuk investasi. Akan tetapi tidak semua wilayah memiliki nilai pertumbuhan nilai properti yang sama, namun pada beberapa daerah mungkin menunjukkan lonjakkan harga yang signifikan karena pembangunan infrastruktur baru, pergeseran demografi, atau peningkatan permintaan pasar. Namun pada dasarnya lonjakan ini bisa bersifat sementara atau disertai dengan fluktuasi harga yang tinggi, yang akan menciptakan ketidakpastian pada nilai aset, namun pada konteks ini pun sebenarnya ada juga wilayah yang menunjukkan pertumbuhan harga yang lebih lambat atau stabil, dengan memiliki resiko investasi yang lebih rendah dan kepastian dari aset yang kita miliki. Dengan melakukan analisis ini, perusahaan dapat menyusun strategi pemasaran dan pengembangan yang berdasarkan potensi dari nilai lokasinya.

## Project Output
Project Output disini saya membuat dasboard analisis property Melbourne, dengan melakukan analisis ini kita dapat melakukan berbagai macam analisis seperti analisis harga analisis ini dapat digunakan juga bagi investor atau perusaan pengembang property untuk mengembangkan segi bisnis mereka. Hasil analisis ini terdapat dalam folder imanges.

## Data
Data yang saya gunakan untuk melakukan analisys ini adalah data yang bersumber dari kaggle, pada dataset ini terdapat jumlah column sebanyak 13 column, lalu untuk baris data sebanyak 63.021, untuk data yang saya gunakan ini adalah data yang telah bersih dari missing values.

## Method
Pada project ini saya menggunakan beberapa metode atau tools, antara lain :
1. Airflow
2. Kibana
3. Elasticsearch
4. Postgres

## Stacks
from datetime import datetime, timedelta
import pandas as pd
import re
from sqlalchemy import create_engine
from elasticsearch import Elasticsearch, helpers
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from great_expectations.data_context import FileDataContext

## Reference
`Bagian ini berisi link pendukung seperti referensi, dashboard, atau deployment`
Link Dataset : [Dataset](https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market)
Link Referensi : [klik here](https://www.theguardian.com/australia-news/article/2024/aug/03/melbourne-house-prices-fall-data-why)
[klik here](https://www.globalpropertyguide.com/pacific/australia/price-history)
---
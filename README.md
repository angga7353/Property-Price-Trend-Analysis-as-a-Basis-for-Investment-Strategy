# Property Price Trend Analysis as a Basis for Investment Strategy

# Problem Background
Dalam industri properti, memahami tren harga di berbagai wilayah merupakan kunci utama bagi investor dan perusahaan pengembang dalam menentukan lokasi strategis untuk investasi. Tidak semua wilayah memiliki pertumbuhan nilai properti yang sama. Beberapa daerah menunjukkan lonjakan harga signifikan akibat pembangunan infrastruktur baru, pergeseran demografi, atau peningkatan permintaan pasar.
Namun, lonjakan harga tersebut bisa bersifat sementara dan sering disertai dengan fluktuasi harga yang tinggi, sehingga menimbulkan ketidakpastian nilai aset. Di sisi lain, terdapat pula wilayah dengan pertumbuhan harga yang lebih lambat namun stabil, yang menawarkan risiko investasi lebih rendah dan memberikan kepastian terhadap nilai aset yang dimiliki.
Dengan melakukan analisis tren harga ini, perusahaan dapat menyusun strategi pemasaran dan pengembangan yang tepat, berdasarkan potensi nilai lokasi yang ada, sehingga memaksimalkan keuntungan sekaligus meminimalkan risiko investasi.

# Project Output
Pada proyek ini, saya membuat dashboard analisis properti di Melbourne. Dashboard ini memungkinkan berbagai jenis analisis, terutama analisis tren harga properti. Hasil analisis ini dapat digunakan oleh investor maupun perusahaan pengembang properti untuk mendukung pengambilan keputusan dan pengembangan strategi bisnis mereka. Visualisasi dan hasil analisis dapat ditemukan dalam folder `images`.

# Data Source
Data yang digunakan dalam analisis ini berasal dari Kaggle. Dataset terdiri dari 13 kolom dan 63.021 baris data. Seluruh data yang digunakan sudah melalui proses pembersihan sehingga tidak mengandung nilai yang hilang (missing values).

# Method
Pada proyek ini, saya menggunakan beberapa metode dan tools berikut untuk mendukung proses analisis dan visualisasi data:
* Apache Airflow
* Kibana
* Elasticsearch
* PostgreSQL

# Library dan Tools yang Digunakan
Pada proyek ini, saya memanfaatkan beberapa teknologi dan library utama untuk membangun pipeline data yang efisien dan dapat diandalkan, antara lain:
* Python Standard Library: Modul datetime dan re digunakan untuk manipulasi tanggal dan regular expression dalam proses data.
* Pandas: Untuk pengolahan dan analisis data secara mudah dan cepat.
* SQLAlchemy: Sebagai alat untuk koneksi dan interaksi dengan database PostgreSQL.
* Elasticsearch & Helpers: Untuk indexing dan pencarian data yang cepat dan scalable.
* Apache Airflow: Digunakan sebagai workflow orchestration tool dengan pendekatan DAG (Directed Acyclic Graph) untuk mengatur task secara terjadwal dan terstruktur.
* Great Expectations: Untuk validasi dan quality check data secara otomatis sebelum proses lanjut.
Dengan kombinasi tools ini, pipeline dapat berjalan secara otomatis dari ekstraksi, transformasi, validasi, hingga loading data ke Elasticsearch, sehingga mendukung analisis data properti secara realtime dan akurat.

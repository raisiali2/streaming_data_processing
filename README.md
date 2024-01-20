# streaming_data_processing

---

## Used Technologies and Services

---

- Item 1 Apache Airflow
- Item 2 Apache Zookeeper
- Item 3 Apache Kafka
- Item 4 Apache Hadoop HDFS
- Item 5 Apache Spark (PySpark)
- Item 6 Hadoop YARN
- Item 7 Elasticsearch
- Item 8 Kibana
- Item 9 MinIO
- Item 10 Docker
- Item 11 OS: Linux 
- Item 12: PyCharm, VSCode

## Overview

- Item 1 Download compressed data source from a URL
- Item 2 processing the downloaded raw data with PySpark, and use HDFS as file storage, check resources with Apache Hadoop YARN.
- Item 3 Use data-generator to simulate streaming data, and send the data to Apache Kafka.
- Item 4 Read the streaming data to Elasticsearchm and visualize it using kibana.
- Item 5 Write the streaming data to MinIO (AWS object Storage) 
- Item 6 Use Apache Airflow to orchestrate the whole data pipeline.

![logo](https://github.com/raisiali2/streaming_data_processing/blob/setup/core-infrastructure/img/plan1.png?raw=true)

---

## Steps of the Project

- Item 1 We should have Apache Kafka, Apache Spark, Apache Hadoop installed locally. Elasticsearch, Kibana and MinIO can be used via docker-compose.yaml.

- Item 2 All steps of the data pipeline can be seen via Airflow DAG. They are all explained here as well.

- Item 3 All scripts were written according to my local file/folder locations. But all mentioned scripts can be found in this repo.

To make Apache Airflow, Docker, Apache Hadoop, Apache Kafka and Apache Zookeeper available, we should run the following commands (This step may differ on how we installed these locally):

'''
sudo systemctl start docker
sudo systemctl start airflow
sudo systemctl start airflow-scheduler
sudo systemctl start zookeeper
sudo systemctl start kafka
start-all.sh
cd /<location_of_docker_compose.yaml>/ && docker-compose up -d '''

## Download the Data:
We should first download the data via the command:

 ' wget -O /<your_local_directory>/sensors.zip https://github.com/dogukannulu/datasets/raw/master/sensors_instrumented_in_an_office_building_dataset.zip '
 
This zip file contains a folder named KETI. Each folder inside this main folder represents a room number. Each room contains five csv files, and each represents a property belonging to these rooms. These properties are:

- Item 1 CO2
- Item 2 Humidity
- Item 3 Light
- Item 4 Temperature
- Item 5 PIR (Passive Infrared Sensor Data)

Each csv also includes timestamp column.

## Unzip the Downloaded Data and Remove README.txt:
We should then unzip this data via the following command:

' unzip /<location_of_zip_file>/sensors_instrumented_in_an_office_building_dataset.zip -d /<desired_location_of_unzipped_folder/ '
Then, we have to remove README.txt since algorithm of the Spark script requires only folders under KETI, not files:

' rm /<location_of_KETI>/KETI/README.txt '

## Put data to HDFS:

KETI folder is now installed to our local successfully. Since PySpark gets the data from HDFS, we should put the local folder to HDFS also using the following sommand:

' hdfs dfs -put /<location_of_KETI>/KETI/ /<desired_location_to_put_KETI>/ '

we can brows for HDFS location we put the data in via localhost:9000

Note: the spark and airflow scripts are run inside virtualenv. the pupose of doing this is not having a library-related issue while running these. the related libraries can be installed globally as well.

## Running the read-write pyspark/pandas script:

both read_and_write_pandas.py and read_and_write_spark.py can be used to modify the initial data. they both do the same job.

all the methods and operations are described with comments and docstrings in both scripts.

we can check localhost:8088 to see the resource usage (YARN) of the running jobs while spark script is runing.

written data:



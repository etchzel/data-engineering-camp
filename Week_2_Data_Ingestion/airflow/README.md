# Data Ingestion

### Table of Contents
- [Data Lake (GCS)]()
    - [What is a data lake?]()
    - [Data Lake vs Data Warehouse]()
    - [Data Lake Gotchas]()
    - [ETL vs ELT]()
    - [Data Lake Cloud Providers]()
- [Workflow Orchestration]()
    - [Introduction to Workflow Orchestration, Airflow and DAG]()
    - [Setting up Airflow]()
        - [Pre-requisites]()
        - [Setup (Lite)]()
        - [Setup (Full)]()
        - [Execution]()
    - [Creating and running a DAG]()
    - [Airflow Tips and Tricks]()
- [Data Ingestion with Airflow]()
    - [Ingesting to local Postgres]()
    - [Ingesting to GCP]()
- [Optional: GCP Transfer Service]()


# Data Lake (GCS)

In this section we learn about Data Lake, comparison with Data Warehouse, various pitfalls that comes with Data Lake, and many more.

## What is a data lake?

Data Lake is a centralized repository for storing, and processing large amounts of structured, semi-structured, and unstructured data. The data can be in its native format (raw).

The idea is to ingest data as quickly as possible, and make it accessible to other team members, like data scientists. Some metadata are generally associated with the data you are ingesting for faster access and better governance of the data in the data lake.

Data Lake are extensively used for machine learning as well as analytical solutions. 

A data lake solution generally has to be:
* Secure
* Scalable
* Inexpensive Hardware

</br>

## Data Lake vs Data Warehouse

Data Lake is a different approach compared to Data Warehouse when it comes to dealing with Big Data. There are several differences from various cases:

* Data Type
    * Data Lake: Generally unstructured data in its native format (raw data).
    * Data Warehouse: Structured data that has been pre-processed and refined for specific purpose.

* Storage
    * Data Lake: Large amounts of data in various formats, in order of petabytes. Can be stored indefinitely.
    * Data Warehouse: Small in comparison to Data Lake. Data is always pre-processed before ingestion and sometimes purged periodically.

* Users
    * Data Lake: Data scientists, data analysts.
    * Data Warehouse: Business analysts.

* Nature
    * Data Lake: **Undefined** and are generally used for wide variety of applications such as Machine Learning, Streaming analytics, and AI.
    * Data Warehouse: Contain historic and **relational** data, such as transaction systems, operations etc. Generally optimized for fast queries.

* Use cases
    * Data Lake: Machine Learning, Stream Processing, Real time analysis.
    * Data Warehouse: Batch Processing, BI, Reporting.

Data Lakes started when companies realized the value of data, they realized that they couldn't store and access data quickly into the Data Warehouse, but didn't want to waste uncollected data when the devs hadn't yet finished developing the data relationships for a Data Warehouse. So, the Data Lake was born to collect any potentially useful data that could later be used in later in the project lifecycle.

</br>

## Data Lake Gotchas

A Data Lake can turn into a *__Data Swamp__* if not managed properly, and therefore makes it very hard to be useful for the consumers of the data. This happens because:

* No versioning of the data
* Incompatible schemas for the same data
    * For example, for the same data, one is stored as Avro, and the next day it is stored as parquet. This makes the data very hard to consume.
* No metadata associated
    * Metadata contains brief information on the actual data. Without this, it will be difficult for the data consumer to navigate through the data lake and find which data is useful for their use case.
* Joins not possible

</br>

## ETL vs ELT

For data ingestion, Data Lakes are generally performed with __ELT__, which is __*Extract, Load, and Transform*__ in comparison to Data Warehouses that use __ETL__ (*__Extract, Transform, and Load__*).

The difference is in the order of steps. In Data Lakes, the data is stored directly without any prior transformations and the schemas will be derived when reading the data (__*Schema on read*__). On the other hand with Data Warehouse, the data is transformed first before and the schemas is decided before hand before loading the data (*__Schema on Write__*).

</br>

## Data Lake Cloud Providers

For the 3 main cloud providers, here are the services they provided that can be used as Data Lake

* Google Cloud Platform : [Cloud Storage](https://cloud.google.com/storage)
* Amazon Web Services   : [Amazon S3](https://aws.amazon.com/s3/)
* Microsoft Azure   : [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)

</br>

# Workflow Orchestration


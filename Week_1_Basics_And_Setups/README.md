# Week 1

## [Docker + PostgreSQL](docker-sql/)
* [Notes](docker-sql/)
* Introduction to Docker
    * Why docker?
    * Creating a simple data pipeline in Docker
* Ingest Data into Postgres Running Locally in Docker
    * Run postgres locally with Docker
    * Query the database using `pgcli`
    * Exploring the data [NY Taxi dataset](https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv)
    * Ingest the data to the database
* Connect Postgres and pgAdmin for a graphical application to interact with the database
    * pgAdmin tool
    * Docker networks
* Putting the ingestion script to Docker
    * Converting an ipynb notebook to a Python script
    * Parametrizing the script with `argparse`
    * Dockerizing the ingestion script
* Running postgres and pgAdmin with `docker-compose`
    * Why `docker-compose`
    * Docker-compose YAML file
    * Running multiple containers with `docker-compose up`
* SQL Refresher
    * Adding the Zones table
    * Inner joins
    * Basic data quality checks
    * Left, Right and Outer joins
    * Group by
* Homework
* Extras on docker networking
    * Docker networks
    * Port forwarding to the host environment
    * Communicating between containers in the network
    * `.dockerignore` file

## [Google Cloud Platform and Terraform](terraform-gcp/)
* [Notes](terraform-gcp/)
* Terraform Basics
* Set up GCP
* Configure IAM and create a service account with proper permissions for the class
* Install `gcloud sdk` locally
* Authenticate credentials for the service account so it can be used locally via `gcloud`
* Enable IAM APIs
* Install terraform
* Set up Terraform files: `main.tf` and `variables.tf`
* Create cloud resources using terraform commands!

## Course Resources
* [Course Repo](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup)
* [YouTube](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
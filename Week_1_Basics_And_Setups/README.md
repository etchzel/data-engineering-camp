# Week 1

## [Docker + PostgreSQL](docker-sql/)
* [Notes](docker-sql/)
* Introduction to Docker
    * Why docker?
    * Creating a simple data pipeline in Docker
* Ingest Data into Postgres Running Locally in Docker
    * Run postgres locally with Docker
    * Query the database using `pgcli`
    * Ingest the data to the database
* Connecting Postgres and pgAdmin with Docker network
    * Installing and configuring pgAdmin in Docker
    * Docker Networks
* Putting the ingestion script to Docker
    * Converting an ipynb notebook to a Python script
    * Parametrizing the script with `argparse`
    * Dockerizing the ingestion script
        * Optional: HTTP server + ipconfig
* Running postgres and pgAdmin with `docker-compose`
    * Why `docker-compose`
    * Docker-compose YAML file
    * Running multiple containers with `docker-compose up`
* SQL Refresher
    * Adding the Zones table
    * Basic query and `INNER JOIN`
    * Basic data quality checks
    * LEFT, RIGHT, and `OUTER JOIN`
    * Dealing with date-like columns and GROUP BY
* Extras on docker networking
    * Docker networks
    * Port forwarding to the host environment
    * Communicating between containers in the network
    * `.dockerignore` file

## [Google Cloud Platform and Terraform](terraform-gcp/)
* [Notes](terraform-gcp/)
* Introduction to Google Cloud Platform
    * GCP setup
    * GCP credentials and SDK
* Terraform
    * Terraform setup
    * Terraform basics
    * Create GCP resource with Terraform

## [Homework](homework/)

## Course Resources
* [Course Repo](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup)
* [YouTube](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
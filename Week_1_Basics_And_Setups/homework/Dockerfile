FROM python:3.8

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY ingest-data.py ingest-data.py
COPY ingest-data-source/output.csv output.csv
COPY ingest-data-source/output-zone.csv output-zone.csv

ENTRYPOINT [ "python", "ingest-data.py" ]
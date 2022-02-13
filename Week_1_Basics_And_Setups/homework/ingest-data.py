import argparse
import os
import pandas as pd
from sqlalchemy import create_engine
from time import time

def check_exist_local(url, filename):
    print('Checking files')

    if os.path.exists(filename):
        print(f'CSV data of {filename} already exists')
    else:
        print('Downloading data')
        os.system(f"wget {url} -O {filename}")

    print('Finished downloading files')


def check_table_exist(table_name, engine):
    # below query check if table exists in the db
    query = f"""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE
                table_name = '{table_name}'
        );
    """
    with engine.connect() as connection:
        result = connection.execute(query).fetchall()

    return result[0][0]


def ingest_data(filename, table_name, engine):
    df_iter = pd.read_csv(filename, iterator=True, chunksize=100000)

    df = next(df_iter)

    if table_name == 'yellow_taxi_trips':
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    while True:
        try:
            t_start = time()
            df.to_sql(name=table_name, con=engine, if_exists='append')
            t_end = time()

            print(f'Ingested {table_name} data chunk, took %.3f second' % (t_end - t_start))

            df = next(df_iter)
            if table_name == 'yellow_taxi_trips':
                df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
                df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
        except StopIteration:
            print('Finished ingesting all the chunks')
            break


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name_trips = params.table_name1
    table_name_zone = params.table_name2
    url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv'
    url2 = 'https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv'
    csv_name = 'output.csv'
    csv_zone_name = 'output-zone.csv'
    engine_uri = f'postgresql://{user}:{password}@{host}:{port}/{db}'

    # check if files exists locally, if not download it
    check_exist_local(url, csv_name)
    check_exist_local(url2, csv_zone_name)
    
    engine = create_engine(engine_uri)

    # check if table exist on the db first, if it is, skip the ingestion
    if not check_table_exist(table_name_trips, engine):
        ingest_data(csv_name, table_name_trips, engine)
    else:
        print(f'Table {table_name_trips} exists in the DB, skipping over the ingestion')

    if not check_table_exist(table_name_zone, engine):
        ingest_data(csv_zone_name, table_name_zone, engine)
    else:
        print(f'Table {table_name_zone} exists in the DB, skipping over the ingestion')

    engine.dispose()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name1', help='name of the table to write results to')
    parser.add_argument('--table_name2', help='name of the table to write results to')
    #parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    main(args)





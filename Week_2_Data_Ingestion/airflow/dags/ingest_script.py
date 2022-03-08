import os

from time import time

import pandas as pd
from sqlalchemy import create_engine

def ingest_callable(user, password, host, port, db, table_name, csv_file, execution_date):
    print(table_name, csv_file, execution_date)

    db_uri = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    engine = create_engine(db_uri)

    with engine.connect() as connection:
        print('connection established successfully, inserting data...')
        t_start = time()
        
        df_iter = pd.read_csv(csv_file, iterator=True, chunksize=100000)
        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

        df.to_sql(name=table_name, con=connection, if_exists='append')

        t_end = time()
        print('Inserted the first chunk, took %.3f second' % (t_end - t_start))

        while True:
            t_start = time()

            try:
                df = next(df_iter)
            except StopIteration:
                print("Completed")
                break

            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name=table_name, con=connection, if_exists='append')

            t_end = time()

            print('Inserted another chunk, took %.3f second' % (t_end - t_start))

    engine.dispose()
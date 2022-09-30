from os import getenv

import pandas as pd
from sqlalchemy import create_engine

import shimoku_api_python as shimoku

from sql_queries import query_clients, query_rooms


business_id: str = getenv('BUSINESS_ID')


def connect_sql_engine() -> create_engine:
    # Get data from a SQL database
    connection_string = 'mysql+pymysql://user:password@host/db'
    conn = create_engine(connection_string)
    return conn


def invoke_shimoku() -> shimoku.Client:
    universe_id: str = getenv('UNIVERSE_ID')
    environment: str = getenv('ENVIRONMENT')

    s = shimoku.Client(
        config={'access_token': api_key},
        universe_id=universe_id,
        environment=environment,
    )
    s.plt.set_business(business_id=business_id)
    return s


# Connect to Shimoku
shimoku = invoke_shimoku()
# Connect to DB
conn = connect_sql_engine()

# Query DB
df_clients = pd.read_sql_query(query_clients, conn)
df_rooms = pd.read_sql_query(query_rooms, conn)

# POST to Shimoku
shimoku.io.post_dataframe(business_id=business_id, app_name='masmvl', filename='clients', df=df_clients)
shimoku.io.post_dataframe(business_id=business_id, app_name='masmvl', filename='rooms', df=df_rooms)

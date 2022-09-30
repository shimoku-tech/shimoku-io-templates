from os import getenv

import pandas as pd

import shimoku_api_python as shimoku


business_id: str = getenv('BUSINESS_ID')


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

# Read csv (from github for example)
df_clients = pd.read_csv('https://raw.githubusercontent.com/rg3915/python-sqlite/master/intermediario/csv/clientes.csv', index_col=0)
df_rooms = pd.read_csv('https://gist.githubusercontent.com/petroniocandido/dbab9321b7d5770b7549682436bb2073/raw/6b41d4a7d1a1f610baed5b0df3802daca8672bc3/products.csv', index_col=0)

# POST to Shimoku
shimoku.io.post_dataframe(business_id=business_id, app_name='masmvl', filename='clients', df=df_clients)
shimoku.io.post_dataframe(business_id=business_id, app_name='masmvl', filename='rooms', df=df_rooms)

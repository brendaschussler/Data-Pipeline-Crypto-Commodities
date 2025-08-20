import pandas as pd
import time
from sqlalchemy import create_engine
from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df

from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv() 

while True:
    df_btc = get_bitcoin_df()
    df_comm = get_commodities_df()

    df = pd.concat([df_btc, df_comm], ignore_index=True)

    print(df)

    time.sleep(60)





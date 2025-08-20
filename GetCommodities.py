import yfinance as yf
from datetime import datetime
import pandas as pd

def get_commodities_df():
    # Simbolo do ativo na bolsa
    tickers = ["GC=F", "CL=F", "SI=F"] # ouro, petroleo, prata

    # crio lista vazia de dataframes
    dfs = []

    for ticker in tickers:
        # Close para pegar a coluna de Close (valor no fechamento)
         # Última cotação (1 minuto)
        df_commodities = yf.Ticker(ticker).history(period="1d", interval="1m")[["Close"]].tail(1)

        # Renomear e adicionar colunas extras
        df_commodities = df_commodities.rename(columns={"Close": "preco"})
        df_commodities["ativo"] = ticker
        df_commodities["moeda"] = "USD"
        df_commodities["horario_coleta"] = datetime.now()

        # Garantir ordem das colunas
        df_commodities = df_commodities[['ativo', 'preco', 'moeda', 'horario_coleta']]

        dfs.append(df_commodities)

    return pd.concat(dfs, ignore_index=True)
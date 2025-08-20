import requests 
from datetime import datetime
import pandas as pd

def get_bitcoin_df():
    # URL da API da Coinbase para o preço do Bitcoin
    url = "https://api.coinbase.com/v2/prices/spot"

    # Faz uma requisição GET para a API
    response = requests.get(url)
    data = response.json()

    # Extrair os dados desejados 
    preco = float(data['data']['amount'])
    ativo = data['data']['base']
    moeda = data['data']['currency']
    horario_coleta = datetime.now()

    # Tranformar as infos em dataframe (estrutura de dados)
    df_bitcoin = pd.DataFrame([{
        'ativo': ativo,
        'preco': preco,
        'moeda': moeda,
        'horario_coleta': horario_coleta
    }])

    return df_bitcoin


import pandas as pd
from pandas import DataFrame
import os
import glob

pasta = 'data'

def extrair(pasta: str)-> DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

def calculo_kpi(df: DataFrame)-> DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df

def carregar(df: DataFrame, tipo_arquivo) -> None:
    if tipo_arquivo == 'csv':
        df.to_csv('dados.csv', index=False)
    elif tipo_arquivo == 'parquet':
        df.to_parquet('dados.parquet')
    else:
        df.to_csv('dados.csv', index=False)
        df.to_parquet('dados.parquet')

def etl_final(pasta: str, arquivo: str)-> None:
    datafame = extrair(pasta)
    calcular = calculo_kpi(datafame)
    carreg = carregar(calcular, arquivo)



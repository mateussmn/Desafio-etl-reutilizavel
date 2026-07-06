import os, glob, pandas as pd
from log import log_decorator
from timer import time_measure_decorator

@log_decorator
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

@log_decorator 
@time_measure_decorator
def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

@log_decorator
def carregar_dados(df: pd.DataFrame ,format_saida : list):
    for formato in format_saida:
        if formato == "csv":
            df.to_csv("dados.csv")
        elif formato == "parquet":
            df.to_parquet('dados.parquet')

    return

@log_decorator
@time_measure_decorator
def pipeline_calculo_kpi(pasta :str, fortmat_saida :list):
    data_frame = extrair_dados(pasta)
    data_frame_total_calculado = calcular_kpi_total_vendas(data_frame)
    carregar_dados(data_frame_total_calculado, ["csv", "parquet"])


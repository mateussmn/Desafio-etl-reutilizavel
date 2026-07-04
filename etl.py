import os, glob, pandas as pd

def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

pasta = 'data'
data_frame = extrair_dados(pasta)
total = calcular_kpi_total_vendas(data_frame)
print(total)

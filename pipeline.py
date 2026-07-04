from etl import pipeline_calculo_kpi

local_pasta: str = "data"
fortmato_saida: list = ["csv"]

pipeline_calculo_kpi(local_pasta, fortmato_saida)
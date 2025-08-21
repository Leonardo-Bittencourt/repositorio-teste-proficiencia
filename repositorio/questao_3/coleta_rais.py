import pandas as pd
from basedosdados import read_sql

# Projeto de cobrança
project_id = "agile-kite-469701-t4"

# Consulta SQL com JOIN para trazer nome do município
query_sql = """
    SELECT 
        e.ano,
        e.sigla_uf,
        e.id_municipio,
        m.nome AS nome_municipio,
        e.cnae_2,
        e.tamanho_estabelecimento,
        e.quantidade_vinculos_ativos
    FROM `basedosdados.br_me_rais.microdados_estabelecimentos` e
    LEFT JOIN `basedosdados.br_bd_diretorios_brasil.municipio` m
      ON e.id_municipio = m.id_municipio
    WHERE e.ano BETWEEN 2019 AND 2023
      AND e.id_municipio IN ('3304557', '3550308')
      AND e.quantidade_vinculos_ativos > 0
"""

print("Buscando dados...")

try:
    df = read_sql(query_sql, billing_project_id=project_id)
    print("Dados recebidos com sucesso!")

    # Salvar em CSV
    df.to_csv("estabelecimentos_rais.csv", index=False, sep=";", encoding="utf-8-sig")
    print("Arquivo 'estabelecimentos_rais.csv' salvo com sucesso!")

except Exception as e:
    print("\n--- OCORREU UM ERRO ---")
    print(e)

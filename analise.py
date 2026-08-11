#Criar aplicação que realizar a limpeza e criação do relatório de importações do ano de 2023, utilizando o arquivo 
# baixado do site da balança comercial.


import pandas as pd

df = pd.read_csv('vendas_reverb.csv', sep=',', encoding='utf-8')

print(df.head())
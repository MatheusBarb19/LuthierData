#Criar aplicação que realizar a limpeza e criação do relatório de importações do ano de 2023, utilizando o arquivo 
# baixado do site da balança comercial.


import pandas as pd

df = pd.read_csv('importacoes_2023.csv', sep=';', encoding='utf-8')


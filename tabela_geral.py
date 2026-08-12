import pandas as pd
import matplotlib.pyplot as plt

# 1. Carrega o arquivo com todos os instrumentos
df = pd.read_csv("todos_instrumentos_reverb.csv")

# 2. Trata a coluna de preço para garantir que seja numérica
df['preco_valor'] = pd.to_numeric(df['preco_valor'], errors='coerce')

# 3. Remove linhas que não possuem marca definida
df_filtrado = df.dropna(subset=['marca'])

# 4. Conta os 10 fabricantes/marcas com mais anúncios registrados
top_marcas = df_filtrado['marca'].value_counts().head(10)

# 5. Configura e desenha o gráfico
plt.figure(figsize=(10, 6))
top_marcas.plot(kind='barh', color='darkcyan')

plt.title('Top 10 Marcas Mais Anunciadas no Reverb', fontsize=14)
plt.xlabel('Quantidade de Anúncios', fontsize=12)
plt.ylabel('Marca', fontsize=12)
plt.gca().invert_yaxis()  # Mantém a maior marca no topo
plt.tight_layout()

# 6. Exibe a imagem na tela
plt.show()
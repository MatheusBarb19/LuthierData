import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("guitarras_gibson_reverb.csv")

# Converte o preço para numérico e remove linhas sem valor
df['preco_valor'] = pd.to_numeric(df['preco_valor'], errors='coerce')

# Plota um gráfico de barras com as 10 guitarras mais caras
top_caras = df.nlargest(10, 'preco_valor')

plt.figure(figsize=(10, 5))
plt.barh(top_caras['titulo'], top_caras['preco_valor'], color='skyblue')
plt.xlabel('Preço')
plt.title('Top 10 Guitarras Gibson Mais Caras Encontradas')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
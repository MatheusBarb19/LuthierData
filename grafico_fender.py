import pandas as pd
import matplotlib.pyplot as plt

# 1. Carrega o CSV geral que você já baixou
df = pd.read_csv("todos_instrumentos_reverb.csv")

# 2. Filtra anúncios que contêm "Fender" na marca ou no título
fender_df = df[df['marca'].str.contains("Fender", case=False, na=False) | 
                df['titulo'].str.contains("Fender", case=False, na=False)].copy()

# Exibe o resumo dos resultados no terminal
print(f"Total de guitarras/instrumentos Fender encontrados: {len(fender_df)}")
print("\n--- Primeiros 5 Resultados ---")
print(fender_df[['titulo', 'preco_valor', 'preco_moeda']].head())

# 3. Converte o preço para valor numérico e remove itens sem preço
fender_df['preco_valor'] = pd.to_numeric(fender_df['preco_valor'], errors='coerce')

# 4. Seleciona as 10 guitarras Fender mais caras
top_caras = fender_df.nlargest(10, 'preco_valor')

# 5. Gera o gráfico de barras
plt.figure(figsize=(10, 5))
plt.barh(top_caras['titulo'], top_caras['preco_valor'], color='crimson')
plt.xlabel('Preço')
plt.title('Top 10 Guitarras Fender Mais Caras Encontradas')
plt.gca().invert_yaxis()
plt.tight_layout()

# 6. Exibe o gráfico na tela
plt.show()
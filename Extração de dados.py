import requests
import pandas as pd

TOKEN = 'dfe78fa42f4ed0b2f9c53199e5292de2784da454bdd25f6db1271dcc19c0bcd5'
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/hal+json',
    'Accept-Version': '3.0'
}

# Parâmetros de busca (ex: Guitarras Fender de $500 a $2000)
params = {
    'query': 'Fender Stratocaster',
    'price_min': 500,
    'price_max': 2000,
    'currency': 'USD',
    'per_page': 50
}

url = 'https://api.reverb.com/api/listings/all'
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    listings = data.get('listings', [])
    
    instrument_data = []
    for item in listings:
        instrument_data.append({
            'id': item.get('id'),
            'titulo': item.get('title'),
            'marca': item.get('make'),
            'modelo': item.get('model'),
            'ano': item.get('finish_year'),
            'preco_valor': item.get('price', {}).get('amount'),
            'moeda': item.get('price', {}).get('currency'),
            'condicao': item.get('condition', {}).get('display_name'),
            'data_criacao': item.get('created_at')
        })
    
    df_reverb = pd.DataFrame(instrument_data)
    df_reverb.to_csv('vendas_reverb.csv', index=False)
    print(f"{len(df_reverb)} instrumentos encontrados e salvos!")
else:
    print(f"Erro na requisição: {response.status_code}")
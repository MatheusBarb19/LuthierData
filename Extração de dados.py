
import requests
import pandas as pd
import time

TOKEN = "5d4b37de4c41d8e9cd4dec84c6ebcf22e7ada2de55e5e2e09727ee7857f61faf"
BASE_URL = "https://api.reverb.com/api/listings/all"

headers = {
    "Accept": "application/hal+json",
    "Accept-Version": "3.0",
    "Authorization": f"Bearer {TOKEN}"
}

def buscar_instrumentos_por_termo(termo_busca="Gibson", total_paginas=5):
    todos_instrumentos = []

    for pagina in range(1, total_paginas + 1):
        params = {
            "query": termo_busca,  # Filtra diretamente por "Gibson"
            "page": pagina,
            "per_page": 50
        }

        response = requests.get(BASE_URL, headers=headers, params=params)
        
        if response.status_code == 200:
            dados = response.json()
            listings = dados.get("listings", [])
            
            if not listings:
                print("Nenhum item adicional encontrado.")
                break
                
            for item in listings:
                instrumento = {
                    "id": item.get("id"),
                    "titulo": item.get("title"),
                    "marca": item.get("make"),
                    "modelo": item.get("model"),
                    "ano": item.get("year"),
                    "condicao": item.get("condition", {}).get("display_name") if item.get("condition") else None,
                    "preco_valor": item.get("price", {}).get("amount") if item.get("price") else None,
                    "preco_moeda": item.get("price", {}).get("currency") if item.get("price") else None,
                    "loja": item.get("shop_name"),
                    "url": item.get("_links", {}).get("web", {}).get("href") if item.get("_links") else None
                }
                todos_instrumentos.append(instrumento)
                
            print(f"Página {pagina} (busca por '{termo_busca}') processada com sucesso!")
            time.sleep(0.5)
        else:
            print(f"Erro na página {pagina}: Status {response.status_code}")
            break

    return pd.DataFrame(todos_instrumentos)

# Testando a busca por Gibson:
df_gibson = buscar_instrumentos_por_termo(termo_busca="Gibson", total_paginas=5)

if not df_gibson.empty:
    df_gibson.to_csv("guitarras_gibson_reverb.csv", index=False, encoding="utf-8-sig")
    print(f"Sucesso! {len(df_gibson)} instrumentos Gibson salvos.")
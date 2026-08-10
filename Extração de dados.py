import requests

url_arquivo = "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/IMP_2023.csv"
caminho_destino = "importacoes_2023.csv"

# O parâmetro stream=True evita carregar o arquivo inteiro na RAM de uma vez
with requests.get(url_arquivo, stream=True) as response:
    response.raise_for_status()
    with open(caminho_destino, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

print("Download concluído com sucesso!")
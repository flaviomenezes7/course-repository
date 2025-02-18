import requests
import pprint

# Buscando o município pelo nome
nome = "Patos de Minas"
url_municipios = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

# Parâmetros para ordenar a lista de municípios pelo nome específico
params = {
    "orderBy": "nome"
}

# Solicitando request
resposta = requests.get(url_municipios, params=params)

# Verificando se o request foi feito com sucesso
try:
    resposta.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"Impossível fazer este request: {e}")
    resultado = None # Caso o request falhe, o resultado será None
else:
    print("Request feito com sucesso")
    resultado = resposta.json()
    
    # Filtrando o resultado para encontrar Patos de Minas
    municipio_filtrado = [mun for mun in resultado if mun['nome'] == nome]
    pprint.pprint(municipio_filtrado)

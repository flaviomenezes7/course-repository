import requests

# Criando o primeiro request

url = 'https://httpbin.org/post'
resposta = requests.get(url)

# DATA = Dados que serão enviados para a API
data = {
    "meus_dados": [1,2,3],
    "pessoa":{
        "nome": "Flávio",
        "idade": 22,
        "aluno": True
}
}

# PARAMS = Parâmetros que serão enviados para a API
params = {
    'dataInicio': '2021-01-01',
    'dataFim': '2021-12-31',
}

#Declarando o método POST e enviando os dados e parâmetros para a API.

resposta = requests.post(url, json=data, params=params)

#print(resposta.json())
print(resposta.request.url)
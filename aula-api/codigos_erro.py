import requests

url = 'https://httpbin.org/post/este/site/nao-existe'

# Solicitando request
resposta = requests.get(url)


# Verificando se o request foi feito com sucesso, caso contrário, exibirá uma mensagem de erro.
try:
    resposta.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"Impossível fazer este request: {e}")
else:
    print(R"Request feito com sucesso")
    print(resposta.json())

import requests

# Criando o primeiro request

url = "https://www.google.com.br"

resposta = requests.get(url)

print(resposta)
print(resposta.text)

with open('pagina_google.html', 'w') as arquivo:
    arquivo.write(resposta.text)
    
# Entendendo os métodos HTTP: GET, POST, PUT, PATCH, DELETE

# GET: Obter informações
# POST: Enviar informações
# PUT: Atualizar informações
# PATCH: Atualizar informações
# DELETE: Deletar informações



import base64
import requests

usuario = "usuario"
senha = "senha"

auth = f"{usuario}:{senha}".encode() # Convertendo para bytes
auth = base64.b64encode(auth) # Codificando para base64
auth = auth.string.decode() # Convertendo para string


url = 'https://httpbin.org/basic-auth/usuario/senha' # Quando a autenticação é feita com sucesso, a API retornará um JSON com a mensagem "authenticated": true
headers = {
    'Authorization': f'Basic {auth}' # Indicando que a autenticação é básica.
    #Barrer tambem é uma outra alternativa para autenticação. Ele é mais seguro por não enviar a senha em texto plano.
}
resposta = requests.get(url, headers=headers) 
try:
    resposta.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"Impossível fazer este request: {e}")
else:
    print("Request feito com sucesso")


# É importante ressaltar que a autenticação básica não é segura, pois a senha é enviada em texto plano.
# Por isso, é recomendado utilizar outros métodos de autenticação, como o OAuth2.
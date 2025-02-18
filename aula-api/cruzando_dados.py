import requests
import pprint

def fazer_request(url, params=None): # Função para fazer request
    resposta = requests.get(url, params=params)
    try: # Verificando se o request foi feito com sucesso
        resposta.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Impossível fazer este request: {e}")
        resultado = None # Caso o request falhe, o resultado será None
    else:
        print("Request feito com sucesso")
        resultado = resposta.json()
    return resultado

def get_state_id(): # Função para obter o id dos estados
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    params = {
        'view': 'nivelado', # Visualizando os estados de forma nivelada
    }
    date_state = fazer_request(url=url, params=params) # Fazendo request para obter os estados
    dict_state = {} # Criando um dicionário vazio
    for date in date_state: # Iterando sobre a lista de estados
        id_state = date['UF-id'] # Obtendo o id do estado
        nome_state = date['UF-nome']  # Obtendo o nome do estado
        dict_state[id_state] = nome_state # Adicionando o id e o nome do estado ao dicionário
    return dict_state

def get_frequency_name_state(nome): # Função para obter a frequência do nome da pessoa que estou pesquisando em cada estado
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'  # Corrigido a formatação da URL
    params = {
        'groupBy': 'UF', # Agrupando por estado
    }
    date_frequency = fazer_request(url=url, params=params) # Fazendo request para obter os estados
    dict_frequency = {} # Criando um dicionário vazio
    for date in date_frequency: # Iterando sobre a lista de estados
       print(date) 
       id_state = int(date['localidade']) # Convertendo o id do estado para inteiro 
       frequency =  date['res'][0]['proporcao'] # Obtendo a frequência do nome no estado conforme a API
       dict_frequency[id_state] = frequency # Adicionando a frequência do nome no estado ao dicionário
    return dict_frequency # Retornando o dicionário com a frequência do nome em cada estado

def main(nome):
    dict_state = get_state_id() # Obtendo o id dos estados
    dict_frequency = get_frequency_name_state(nome=nome) # Obtendo a frequência do nome em cada estado
    print(f'--- Frequência do nome "{nome}" nos Estados (por 100.000 habitantes)')
    for id_state, nome_state in dict_state.items():  # Corrigido: iterando sobre dict_state ao invés de dict_frequency
        frequency_state = dict_frequency.get(id_state, 0)  # Usando .get() para evitar KeyError
        print(f'-> {nome_state}: {frequency_state}')
        
if __name__ == "__main__":
    main("Juliano") # Chamando a função main com o nome específico.
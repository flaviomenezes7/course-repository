import requests
import pprint
import pandas as pd
import streamlit as st

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

def pegar_nome_por_decada(nome): # Função para obter a frequência do nome da pessoa que estou pesquisando em cada estado
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'  # Corrigido a formatação da URL
    dados_decadas = fazer_request(url=url) # Fazendo request para obter os estados
    if not dados_decadas:
        return {} # Caso o request falhe, retornar um dicionário vazio
    dict_decadas = {}
    for dados in dados_decadas[0]['res']: # Buscando uma pessoa por vez
        decada = dados['periodo']
        quantidade = dados['frequencia']
        dict_decadas[decada] = quantidade
    return dict_decadas

def main(nome):
    st.title('Web App - Nomes')
    st.write('API Dados do IBGE')
    
    nome = st.text_input('Consulte um nome:')
    if not nome:
        st.stop()
        
    dict_decadas = pegar_nome_por_decada(nome)
    if not dict_decadas:
        st.warning('Nome não encontrado.')
        st.stop()
    df = pd.DataFrame.from_dict(dict_decadas, orient='index')
    
    col1, col2 = st.columns([0.3, 0.7]) # Dividindo a tela em duas colunas e ocupando 30% e 70% do espaço, respectivamente
    with col1:
        st.write('Frequência por decadas')
        st.dataframe(df)
    with col2:
        st.write('Evolução do nome por décadas')
        st.line_chart(df)
        

    st.write('---')
    st.write('Fonte: https://servicodados.ibge.gov.br/api/docs/')
    
if __name__ == "__main__":
    
    main("") # Chamando a função main com o nome específico.
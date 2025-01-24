import requests

# API_KEY = "SwsD2SXhef7mXTjrnYKPgzy11SyrWjNu56Pz8ipVpNEPSteG1q8GF5za0PhD"
URL_BASE = "https://receitaws.com.br/v1/cnpj/{cnpj}"

def buscar_dados_cnpj(cnpj):
    # Remover pontos, barras e traços do CNPJ para garantir que está no formato correto
    cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")
    
    try:
        # Fazendo a requisição GET para a API
        response = requests.get(URL_BASE.format(cnpj=cnpj))

        response.raise_for_status()  # Lança um erro se a resposta for 4xx ou 5xx
        
        # Converte a resposta em JSON
        dados = response.json()

        # Verifica se o CNPJ foi encontrado e se contém a chave 'status' para indicar erro
        if dados.get("status") == "ERROR":
            print(f"Erro ao buscar CNPJ {cnpj}: {dados.get('message')}")
            return None
        
        return dados

    except requests.exceptions.HTTPError as errh:
        print(f"Erro HTTP: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Erro ao buscar CNPJ {cnpj}: {err}")
    return None

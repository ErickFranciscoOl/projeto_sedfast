import requests
from utils.extracao import extrair_primeiro_ultimo_nome

API_KEY = "yKrbkWVxKMziuApyvYHy9Q"  # ✅ Definição da API_KEY corrigida

def buscar_socio_apollo(nome_completo_socio, empresa):
    """
    Busca um sócio na API Apollo utilizando nome parcial e filtrando pela empresa.
    """
    url = "https://api.apollo.io/api/v1/mixed_people/search"
    
    nome_parcial = extrair_primeiro_ultimo_nome(nome_completo_socio)  # ✅ Passando parâmetro correto
    nome_parcial = f"{nome_parcial[0]} {nome_parcial[1]}".strip()  # ✅ Garante que sempre há uma string válida

    payload = {
        "api_key": API_KEY,  
        "q_name": nome_parcial,  # ✅ Usa nome parcial corretamente
        "q_organization_name": empresa,  
        "page": 1,
        "per_page": 1  
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        if "people" in data and data["people"]:
            pessoa = data["people"][0]
            return {
                "Nome": pessoa.get("name"),
                "Cargo": pessoa.get("job_title"),
                "Empresa": pessoa.get("organization", {}).get("name"),
                "Email": pessoa.get("emails", ["Não disponível"])[0],  
                "Telefone": ", ".join(pessoa.get("phones", ["Não disponível"]))  
            }
        else:
            print(f"❌ Nenhum resultado encontrado para {nome_completo_socio} na empresa {empresa}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"⚠ Erro ao buscar sócio {nome_completo_socio}: {e}")
        return None

from services.consulta_cnpj import buscar_dados_cnpj
from services.consulta_socios import buscar_socio_apollo
from utils.extracao import extrair_dois_primeiros_nomes, extrair_primeiro_ultimo_nome
from utils.file_manager import ler_cnpjs_csv, salvar_dados_excel

# Caminho do arquivo CSV com os CNPJs
CAMINHO_CSV = r"C:\Users\Fastcash Analista\Documents\Projeto SEDFAST\data\empresas.csv"
CAMINHO_EXCEL = r"C:\Users\Fastcash Analista\Documents\Projeto SEDFAST\data\dados_enriquecidos.xlsx"

# Lista de CNPJs a serem processados
cnpjs = ler_cnpjs_csv(CAMINHO_CSV)

# Lista para armazenar os resultados
dados_final = []

for cnpj in cnpjs:
    # Buscar dados da empresa
    empresa = buscar_dados_cnpj(cnpj)

    if empresa:
        nome_empresa = extrair_dois_primeiros_nomes(empresa["nome"])  # ✅ Corrigido
        for socio in empresa.get("qsa", []):  # ✅ Acessa "qsa" corretamente
            nome_socio = socio["nome"]  # ✅ Obtém o nome do sócio corretamente
            primeiro_nome, segundo_nome = extrair_primeiro_ultimo_nome(nome_socio)  # ✅ Extrai corretamente
            dados_socio = buscar_socio_apollo(f"{primeiro_nome} {segundo_nome}", nome_empresa)  # ✅ Passa corretamente

            # Adicionar ao resultado final
            dados_final.append({
                "CNPJ": empresa["cnpj"],
                "Nome_Empresa": empresa["nome"],
                "Telefone_Empresa": empresa.get("telefone", ""),
                "Email_Empresa": empresa.get("email", ""),
                "Nome_Sócio": nome_socio,
                "Email_Sócio": dados_socio.get("Email") if dados_socio else "",
                "Telefone_Sócio": dados_socio.get("Telefone") if dados_socio else "",
                "LinkedIn_Sócio": dados_socio.get("LinkedIn") if dados_socio else ""
            })

# Salvar os dados coletados no Excel
salvar_dados_excel(dados_final, CAMINHO_EXCEL)

print("\n✅ Automação concluída! Dados salvos em:", CAMINHO_EXCEL)

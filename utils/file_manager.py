import pandas as pd

def ler_cnpjs_csv(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo, sep=",", encoding="utf-8", dtype=str)  # Força os CNPJs a serem strings
    df["CNPJ"] = df["CNPJ"].str.replace(r"[^\d]", "", regex=True)  # Remove pontos e barras
    print(df.head())  # Verifica se os dados estão corretos
    return df["CNPJ"].tolist()

def salvar_dados_excel(dados, caminho_saida):
    df = pd.DataFrame(dados)  # Converte os dados para DataFrame
    df.to_excel(caminho_saida, index=False, engine="openpyxl")  # Salva no Excel
    print(f"Arquivo salvo em: {caminho_saida}")

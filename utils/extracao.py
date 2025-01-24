def extrair_primeiro_ultimo_nome(nome_completo):
    partes = nome_completo.split()
    if len(partes) >= 2:
        return partes[0], partes[-1]  # ✅ Retorna uma tupla com dois valores
    return partes[0], "" if partes else ("", "")  # ✅ Retorna dois valores sempre

def extrair_dois_primeiros_nomes(nome_empresa):
    partes = nome_empresa.split()
    return " ".join(partes[:2])  # ✅ Corrigido espaço extra no join

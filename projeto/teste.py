import requests

def modelo_existe(marca_nome, modelo_nome):
    # 1) Buscar lista de marcas
    marcas = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas").json()
    
    # Procurar código da marca pelo nome digitado
    marca_codigo = None
    for marca in marcas:
        if marca["nome"].lower() == marca_nome.lower():
            marca_codigo = marca["codigo"]
            break
    
    if marca_codigo is None:
        return False, f"Marca '{marca_nome}' não encontrada."
    
    # 2) Buscar lista de modelos da marca
    url_modelos = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_codigo}/modelos"
    modelos = requests.get(url_modelos).json()
    
    # 3) Verificar se o modelo existe
    for modelo in modelos:
        if modelo_nome.lower() in modelo["nome"].lower():  # Aceita correspondência aproximada
            return True, f"Modelo encontrado: {modelo['nome']}"
    
    return False, f"Modelo '{modelo_nome}' não encontrado para a marca '{marca_nome}'."

# -----------------------------
# Exemplo de uso:
existe, mensagem = modelo_existe("Fiat", "Argo")
print(mensagem)
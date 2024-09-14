import requests

# URL base da API pública de Warframe para Warframes
BASE_URL = "https://api.warframestat.us/warframes"

def obter_warframes(idioma='pt'):
    """
    Obtém a lista de Warframes e suas informações, com suporte a múltiplos idiomas.
    """
    try:
        response = requests.get(BASE_URL, params={'language': idioma})
        response.raise_for_status()  # Verifica se a requisição foi bem sucedida
        return response.json()  # Retorna os dados no formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter dados: {e}")
        return None

def exibir_warframes(idioma='pt'):
    """
    Exibe informações sobre os Warframes, incluindo habilidades e duas características principais.
    """
    warframes = obter_warframes(idioma)

    if warframes:
        for warframe in warframes:
            print(f"Nome: {warframe['name']}")
            print(f"Descrição: {warframe['description']}")
            print(f"Saúde: {warframe['health']}")
            print(f"Escudos: {warframe['shield']}")
            print("\nHabilidades:")
            for habilidade in warframe['abilities']:
                print(f"  - {habilidade['name']}: {habilidade['description']}")
            print("-" * 50)
    else:
        print("Não foi possível obter informações dos Warframes.")

if __name__ == "__main__":
    exibir_warframes()

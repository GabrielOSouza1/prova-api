import requests


BASE_URL = "https://api.warframestat.us/warframes"

def obter_warframes(idioma='pt'):
    
    try:
        response = requests.get(BASE_URL, params={'language': idioma})
        response.raise_for_status()  
        return response.json()  
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter dados: {e}")
        return None

def exibir_warframes(idioma='pt'):
    
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

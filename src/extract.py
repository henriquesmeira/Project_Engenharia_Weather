import os
import json
import requests
import logging
from pathlib import Path
from dotenv import load_dotenv

# Configura o caminho base (onde o extract.py está -> sobe para a raiz)
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_weather_data(city_name: str) -> dict:
    # IMPORTANTE: Verifique se no seu .env está exatamente 'OpenWeather' ou 'API_KEY'
    api_key = os.getenv('API_KEY') 
    
    if not api_key:
        logging.error("API Key não encontrada! Verifique o nome no arquivo .env")
        return None

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}'
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        
        # Define o caminho para salvar na pasta 'data' na raiz do projeto
        output_path = BASE_DIR / 'data' / 'weather_data.json'
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        logging.info(f"Dados de {city_name} salvos com sucesso em: {output_path}")
        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"Erro na requisição: {e}")
        return None

if __name__ == "__main__":
    extract_weather_data("Uba,BR")
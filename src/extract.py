import os
from dotenv import load_dotenv
from google.cloud import storage

# 1. Carrega as variáveis do arquivo .env
load_dotenv()

def upload_to_local_gcp():
    # Pega as configurações
    bucket_name = os.getenv("GCS_BUCKET_NAME")
    storage_host = os.getenv("STORAGE_EMULATOR_HOST")
    
    # 2. Configura o Python para olhar para o Docker (LocalStack/Fake-GCS)
    # Sem isso, ele tentaria conectar na internet e daria erro de senha
    os.environ["STORAGE_EMULATOR_HOST"] = storage_host
    
    print(f"📡 Conectando ao simulador Cloud em: {storage_host}")
    
    try:
        # Inicializa o cliente (no simulador, não pede senha)
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        
        # 3. Define o arquivo de origem e o destino
        source_file = "data/weather_data.csv"
        destination_blob = "raw/weather_v1.csv"
        
        # Faz o upload
        blob = bucket.blob(destination_blob)
        blob.upload_from_filename(source_file)
        
        print(f"✅ SUCESSO! O arquivo '{source_file}' foi enviado para o bucket '{bucket_name}'.")
        print(f"🔗 Link local: {storage_host}/{bucket_name}/{destination_blob}")

    except Exception as e:
        print(f"❌ ERRO: {e}")

if __name__ == "__main__":
    upload_to_local_gcp()
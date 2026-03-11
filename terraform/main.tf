terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region

  # Adicione estas duas linhas:
  access_token = "fake-token" # Engana o validador de credenciais
  user_project_override = true

  # Mantém o seu endpoint local
  storage_custom_endpoint = "http://localhost:4443/storage/v1/"
}

resource "google_storage_bucket" "meu_bucket" {
  name          = var.bucket_name
  location      = "US"
  force_destroy = true
  
  # O simulador local não exige algumas travas de segurança da nuvem real
  public_access_prevention = "inherited"
}
variable "project_id" {
  description = "ID do projeto GCP"
  default     = "Weather"
}

variable "bucket_name" {
  description = "Weather"
  default     = "bucket-weather-raw"
}

variable "region" {
  default     = "us-central1"
}
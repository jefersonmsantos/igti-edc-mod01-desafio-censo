variable "aws_region" {
    default = "sa-east-1"
}

variable "airflow_subnet_id" {
    default = "subnet-0c2d4f69"
}

variable "lambda_function_name" {
    default = "IGTIDownloadExtract"
}

variable "key_pair_name" {
    default = "jeferson=igti-teste2"
}

variable "vpc_id"{
    default = "vpc-f60e6393"
}
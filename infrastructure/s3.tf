resource "aws_s3_bucket" "datalake" {
    #Parâmetros de coniguração
    bucket = "datalake-igti-mod01-desafio"
    acl = "private"
    
    server_side_encryption_configuration {
        rule {
            apply_server_side_encryption_by_default {
                sse_algorithm = "AES256"
            }
        }
    }

    tags = {
        IES = "IGTI",
        CURSO = "EDC"
    }
}
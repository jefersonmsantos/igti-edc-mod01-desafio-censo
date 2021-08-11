resource "aws_lambda_function" "download_extract" {
    filename = "lambda_function_payload.zip"
    function_name = var.lambda_function_name
    role = aws_iam_role.lambda.arn 
    handler = "lambda_function_download_extract.handler"
    memory_size = 12000  
    timeout = 900

    source_code_hash = filebase64sha256("lambda_function_payload.zip")

    runtime = "python3.8"

    tags = {
        IES = "IGTI"
        CURSO = "EDC"
    }
}
resource "aws_s3_bucket_object" "codigo_spark" {
    bucket = aws_s3_bucket.datalake.id
    key = "emr-code/pyspark/csv_to_parquet_job_spark.py"
    acl = "private"
    source = "../etl/csv_to_parquet_job_spark.py"
    etag = filemd5("../etl/csv_to_parquet_job_spark.py")
}

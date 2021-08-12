resource "aws_glue_catalog_database" "censo" {
  name = "censo-escolar"
}

resource "aws_glue_crawler" "censo" {
  database_name = aws_glue_catalog_database.censo.name
  name          = "censo_escolar_s3_crawler"
  role          = aws_iam_role.glue_role.arn

  s3_target {
    path = "s3://${aws_s3_bucket.datalake.bucket}/staging/"
  }

  configuration = <<EOF
{
   "Version": 1.0,
   "Grouping": {
      "TableGroupingPolicy": "CombineCompatibleSchemas" }
}
EOF

  tags = {
    IES   = "IGTI",
    CURSO = "EDC"
  }
}
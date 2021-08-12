from pyspark.sql.functions import mean, max, min, col,count
from pyspark.sql import SparkSession
import s3fs
#import boto3

#spark = (SparkSession.builder.appName("DeltaExercise")
#    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.0.0")
#    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
#    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
#    .getOrCreate()
#)

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

#from delta.tables import *
#s3 = boto3.resource('s3')
#bucket = s3.Bucket('datalake-igti-mod01-desafio')

#for obj in bucket.objects.all():
        
#    if str(obj.key)[-3:].lower() == "csv":
        
        #file_name = obj.key.split("/")[-1]

fs = s3fs.S3FileSystem(anon=False)

for obj in fs.ls('datalake-igti-mod01-desafio'):
    if obj[-3:].lower() == 'csv':

        raw_file = (
                spark
                .read
                .format("csv")
                .option("header", True)
                .option("inferSchema",True)
                .option("delimiter","|")
                .option("encoding","utf-8")
                .load('s3://datalake-igti-mod01-desafio/'+obj)
            )

        file_name = obj.split("/")[-1][:-4]

        #salvar parquet
        (
            raw_file
            .write
            .mode("overwrite")
            .format("parquet")
            .save('s3://datalake-igti-mod01-desafio/staging/'+file_name)
        )
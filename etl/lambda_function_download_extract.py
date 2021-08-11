import boto3
import urllib3
import zipfile
from io import BytesIO

#Criar cliente para interagir com S3
s3 = boto3.resource('s3')
url = 'https://download.inep.gov.br/dados_abertos/microdados_censo_escolar_2020.zip'
http=urllib3.PoolManager()
bucket = s3.Bucket('datalake-igti-mod01-desafio')

def handler(event, context):
    #download file
    s3.meta.client.upload_fileobj(http.request('GET', url, preload_content=False), 'datalake-igti-mod01-desafio', Key = "download-area/censo-escolar-2020.zip")
    
    
    
    for obj in bucket.objects.all():
        
        if str(obj.key)[-3:].lower() == "zip":
        
            zf = zipfile.ZipFile(BytesIO(obj.get()['Body'].read()),"r")
        
            with zf as zip_archive:
                for item in zip_archive.filelist:
                    if (item.filename[-1]!="/") & (item.filename[-3:].lower()=="csv"):
                        with zf.open(item) as i:
                            filebytes = i.read()
        
                            folder = item.filename.split("/")[-1][:-3]
                            file_name = item.filename.split("/")[-1]
        
                            s3.meta.client.upload_fileobj(BytesIO(filebytes), 'datalake-igti-mod01-desafio', Key = "raw-data/"+folder + "/" + file_name)
        
                            print("Uploaded "+file_name)





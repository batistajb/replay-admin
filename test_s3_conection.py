import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError

load_dotenv()

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_S3_REGION_NAME')
)

bucket_name = os.getenv('AWS_STORAGE_BUCKET_NAME')


def list_files_in_bucket():
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print("Bucket vazio ou inacessível.")
    except Exception as e:
        print(f"Erro ao acessar o bucket: {e}")


# def upload_file_to_bucket():
#     """Faz o upload para o bucket."""
#     try:
#         file_content = "Este é um arquivo de teste enviado para o S3."
#         file_name = "teste_upload_s3.txt"

#         # Fazendo upload do arquivo
#         s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)

#         print(f"Arquivo '{file_name}' enviado com sucesso para o bucket '{bucket_name}'.")
#     except NoCredentialsError:
#         print("Credenciais não encontradas. Verifique as configurações.")
#     except Exception as e:
#         print(f"Erro ao enviar o arquivo: {e}")


if __name__ == "__main__":
    print("Listando arquivos no bucket:")
    list_files_in_bucket()

    # print("\nFazendo upload de um arquivo:")
    # upload_file_to_bucket()

    # print("\nListando arquivos no bucket novamente:")
    # list_files_in_bucket()

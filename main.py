import boto3
s3_client = boto3.client('s3')
s3 = boto3.resource('s3')
s3.Bucket('filenotuploaded')
s3.meta.client.upload_file(r"C:\Users\h_ram\OneDrive\Desktop\example.txt.txt",'filenotuploaded','example1.txt')
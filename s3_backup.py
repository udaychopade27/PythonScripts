import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket=bucket_name, 
                     CreateBucketConfiguration={
                         'LocationConstraint': region,
                     },)
    print("Bucket created successfully")

def upload_backup(s3, file_name, bucket_name, key_name):
    data = open(file_name, 'rb')  # this line open file and read it in binary
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)  #key_name= file name for backup file to store in s3
    print("backup uploaded successfully")


bucket_name = "pythonbackupupload"
region = "ap-south-1"
file_name = "/home/nimap/uday/Programming/Python/backups/backup_2024-10-01.tar.gz"
key_name = "backupUsingPython_2024-10-01.tar.gz"
create_bucket(s3, bucket_name, region)
show_buckets(s3)
upload_backup






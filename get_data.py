import boto3
import pandas as pd


## Create a client S3 
s3_client = boto3.client('s3')
print(s3_client)

# Use the client S3 to list buckets
buckets = s3_client.list_buckets()
for bucket in buckets['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')

# Connect to my resource to list my buckets and files including in
s3 = boto3.resource('s3')
bucket = s3.Bucket('s3bucketdatalake12')
print(list(bucket.objects.all()))


# Open a file from S3 bucket into here and then download in my repo
obj = s3.Bucket('s3bucketdatalake12').Object('50_Startups.csv').get()
df = pd.read_csv(obj['Body'])
df.to_csv("Startups.csv",mode='a')
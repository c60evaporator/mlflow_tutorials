# %%
import boto3
import os
# アップロード用のテキストファイル作成
text = 'rooms, zipcode, median_price, school_rating, transport'
text_path = 'fuga.txt'
with open(text_path, 'w') as f:
    f.write(text)
# S3にアップロード
s3 = boto3.resource('s3', aws_access_key_id='', aws_secret_access_key='')
bucket = s3.Bucket('mlflow-policy-test')
bucket.upload_file(text_path, text_path)
os.remove(text_path)
# %%

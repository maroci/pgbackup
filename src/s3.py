import boto3

from pgbackup import storage

client.boto3.client('s3')
infile = open('example.txt','rb')
storage.s3(client, infile, 'python-backups',infile.name)
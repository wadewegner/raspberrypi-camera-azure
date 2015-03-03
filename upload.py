import sys
import os
import ConfigParser
from azure.storage import BlobService

config = ConfigParser.ConfigParser()
config.read('config.ini')

accountName = config.get('Storage', 'AccountName')
accountKey = config.get('Storage', 'AccountKey')

fileName = sys.argv[1]
type = sys.argv[2]

if type == "jpg":
	type = "image/jpg"
elif type == "mp4":
	type = "video/mp4"
elif type == "txt":
	type = "text/plain"
else:
	print "Not a valid type"
	sys.exit()

blob_service = BlobService(account_name=accountName, account_key=accountKey)

blob_service.put_block_blob_from_path(
	'public',
	fileName,
	fileName,
	x_ms_blob_content_type=type
)

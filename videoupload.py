from subprocess import call
from azure.storage import BlobService
import time
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

accountName = config.get('Storage', 'AccountName')
accountKey = config.get('Storage', 'AccountKey')

blob_service = BlobService(account_name=accountName, account_key=accountKey)

videoName = str(time.time())

recordCommand = "raspivid -o " + videoName + ".h264"
call ([recordCommand], shell=True)

convertCommand = "MP4Box -add " + videoName + ".h264 " + videoName + ".mp4"
call ([convertCommand], shell=True)

blob_service.put_block_blob_from_path(
	'public',
	videoName + '.mp4',
	videoName + '.mp4',
	x_ms_blob_content_type='video/mp4'
)

print 'http://' + accountName + '.blob.core.windows.net/public/' + videoName + '.mp4'

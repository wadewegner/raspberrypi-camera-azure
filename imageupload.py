from azure.storage import BlobService
import picamera
import time

camera = picamera.PiCamera()

accountName = ""
accountKey = ""

ticks = time.time()
imageName = str(ticks) + '.jpg'

camera.vflip = True

camera.capture(imageName)

blob_service = BlobService(account_name=accountName, account_key=accountKey)

blob_service.put_block_blob_from_path(
	'public',
	imageName,
	imageName,
	x_ms_blob_content_type='image/jpg'
)

print 'http://' + accountName + '.blob.core.windows.net/public/' + imageName

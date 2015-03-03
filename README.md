# raspberrypi-camera-azure

Some hackery with the Raspberry Pi Camera using Azure storage.

To use this code, simply update `config.ini` to use your own Azure storage account.

You can run the following scripts:

    python upload.py FILENAME TYPE (i.e. jpg, mp4, or txt)
    python imageupload.py
    python videoupload.py

To use the `picamera`, `azure`, and `MP4Box` run the following commands:

    sudo apt-get install python-picamera

    curl https://bootstrap.pypa.io/get-pip.py | sudo python
    sudo pip install azure
    
    sudo apt-get install gpac
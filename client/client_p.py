import requests
import os
import mimetypes


SERVER_URL = "http://localhost:8000"

files_to_send = ['./logs.txt']

def cf():
    for filename in files_to_send:
        if not os.path.exists(filename):
            open(filename, "w")

def sf():
    cf()

    for filepath in files_to_send:
        if not os.path.exists(filepath):continue
        try:
            with open(filepath, 'rb') as f:
                mimetype, _ = mimetypes.guess_type(filepath)
                mimetype = mimetype or 'application/octet-stream'
                files = {'file': (os.path.basename(filepath), f, mimetype)}
                requests.post(SERVER_URL, files=files)
        except:pass
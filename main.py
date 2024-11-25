from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", 'text/html')
        self.end_headers()
        with open('contact.html', 'r', encoding="UTF-8") as f:
            file = f.read()
        self.wfile.write(file.encode('utf-8'))

    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        body = self.rfile.read(content_len)
        print(body)
        decoded_body = body.decode('utf-8')  # Декодируем байты в строку
        print("Received POST data:", decoded_body)
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


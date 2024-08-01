from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import subprocess
import threading


class RedirectHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Redirect to the new HTML page
        self.send_response(301)
        self.send_header('Location', 'http://10.0.0.201/index.html')  # Replace with the actual IP and page
        self.end_headers()


def run(server_class=HTTPServer, handler_class=RedirectHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()


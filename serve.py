import http.server, os, socketserver
port = int(os.environ.get("PORT", "8077"))
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", port), H) as httpd:
    print(f"serving on {port}", flush=True)
    httpd.serve_forever()

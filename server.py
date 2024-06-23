from http.server import HTTPServer, SimpleHTTPRequestHandler
from config import USERNAME, PASSWORD
import base64
import ssl

username = USERNAME
password = PASSWORD

# Create a subclass of SimpleHTTPRequestHandler to handle authentication/HTTP requests
class AuthHandler(SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self._authenticate()
        return super().do_HEAD()

    def do_GET(self):
        if not self._authenticate():
            return
        return super().do_GET()
    
    def do_POST(self):
        if not self._authenticate():
            return
        return super().do_POST()
    
    def _authenticate(self):
        # get authorization header from request
        auth_header = self.headers.get('Authorization') 
        if auth_header is None or not self._check_credentials(auth_header):
            self.send_response(401)
            # request basic authentication
            self.send_header('WWW-Authenticate', 'Basic realm=\"File Server\"') 
            self.end_headers() # end HTTP headers
            self.wfile.write(b'Authentication required')
            return False 
        return True
    
    def _check_credentials(self, auth_header):
        # split authorization header into auth type and encoded credentials
        auth_type, encoded_credentials = auth_header.split()
        # decode the base64 encoded credentials
        credentials = base64.b64decode(encoded_credentials).decode()
        # split the credentials into username and password
        user, passwd = credentials.split(':')
        # check if provided username and password match the expected ones
        return user == username and passwd == password
        
if __name__ == '__main__':
    port = 5000  
    server_address = ('', port)  # Define the server address (empty string means all interfaces)
    httpd = HTTPServer(server_address, AuthHandler)
    
    # Configure SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='.certificate.pem', keyfile='.key.pem') 
    
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True) 
    
    try:
        print(f'Server live on port {port}')
        httpd.serve_forever() 
    except KeyboardInterrupt:
        print('Server shutting down')
        httpd.shutdown()
        httpd.server_close()
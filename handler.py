from functools import partial
from http.server import SimpleHTTPRequestHandler, test
import base64
import os


class AuthHTTPRequestHandler(SimpleHTTPRequestHandler):
    """ Main class to present webpages and authentication. """

    def __init__(self, *args, **kwargs):
        username = kwargs.pop("username")
        password = kwargs.pop("password")
        self._auth = base64.b64encode(
            f"{username}:{password}".encode()).decode()
        super().__init__(*args, **kwargs)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Test"')
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """ Present frontpage with user authentication. """
        if self.headers.get("Authorization") == None:
            self.do_AUTHHEAD()
            self.wfile.write(b"no auth header received")
        elif self.headers.get("Authorization") == "Basic " + self._auth:
            SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.do_AUTHHEAD()
            self.wfile.write(self.headers.get("Authorization").encode())
            self.wfile.write(b"not authenticated")


if __name__ == "__main__":

    handler_class = partial(
        AuthHTTPRequestHandler,
        username=os.environ.get("USERNAME"),
        password=os.environ.get("PASSWORD"),
        directory='/data',
    )
    test(HandlerClass=handler_class, port=os.environ.get('PORT'))

class ZezereSecurityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Content-Security-Policy"] = (
            "default-src http://localhost:8080; "
            + "style-src https://unpkg.com/ 'nonce-ii98asdj23dfn2';"
            + "script-src https://unpkg.com/ https://cdnjs.cloudflare.com/ http://localhost:8080;"
            + "font-src https://unpkg.com/;"
        )
        return response

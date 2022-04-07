sni = "cdn.zoom.us"


class Proxy:
    def tls_start_client(self, data):
        data.conn.sni = sni

    def tls_start_server(self, data):
        data.conn.sni = sni


addons = [Proxy()]

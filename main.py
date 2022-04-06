sni = "cdn.zoom.us"


class Proxy:
    # def request(self, flow):
    #     flow.client_conn.tls = False

    #     client_state = flow.client_conn.get_state()
    #     client_state["sni"] = sni
    #     flow.client_conn.set_state(client_state)

    #     server_state = flow.server_conn.get_state()
    #     server_state["sni"] = sni
    #     flow.server_conn.set_state(server_state)

    def tls_start_client(self, data):
        data.conn.sni = sni

    def tls_start_server(self, data):
        data.conn.sni = sni


addons = [Proxy()]

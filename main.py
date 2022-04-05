from mitmproxy import ctx


class Proxy:
    def request(self, flow):
        sni = "cdn.zoom.us"
        client_state = flow.client_conn.get_state()
        client_state["sni"] = sni
        flow.client_conn.set_state(client_state)

        # server_state = flow.server_conn.get_state()
        # server_state["sni"] = sni
        # flow.server_conn.set_state(server_state)


addons = [Proxy()]

import json
from user import User
from urllib.parse import urlparse
import http.client
import requests


class Client:
    _muUrl = ''
    _muKey = ''
    _nodeId = 1

    def __init__(self, mu_url, node_id, mu_key):
        self._muUrl = mu_url
        self._nodeId = node_id
        self._muKey = mu_key

    def _gen_users_url(self):
        return "%s/nodes/%d/users".format(self._muUrl, self._nodeId)

    def _gen_node_traffic_url(self):
        return "%s/nodes/%d/traffic".format(self._muUrl, self._nodeId)

    def _gen_headers(self):
        headers = {
            'Token': self._muKey
        }
        return headers

    def get_url(self):
        return self._muUrl

    def update_traffic(self):
        pass

    def get_users_res(self):
        url = self._gen_users_url()
        o = urlparse(url)

        conn = http.client.HTTPConnection(o.netloc)
        headers = self._gen_headers()
        conn.request("GET", o.path, headers=headers)

        res = conn.getresponse()
        data = res.read()
        return data.decode('utf-8')

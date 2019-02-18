#!/usr/bin/env python3

import base64
import json
import requests
import sseclient

BITDB_URL     = 'https://bitdb.fountainhead.cash/q/'
BITSOCKET_URL = 'https://bitsocket.fountainhead.cash/s/'

def query_bitdb(query):
    json_string = bytes(json.dumps(query), 'utf-8')
    url = base64.b64encode(json_string)
    r = requests.get(BITDB_URL + url.decode('utf-8'))

    return r.json()


def query_bitsocket(query, fn):
    json_string = bytes(json.dumps(query), 'utf-8')
    url = base64.b64encode(json_string)
    r = requests.get(BITSOCKET_URL + url.decode('utf-8'), stream=True)

    client = sseclient.SSEClient(r)
    for evt in client.events():
        fn(json.loads(evt.data))


if __name__ == "__main__":
    query = {
        "v": 3,
        "q": {
            "find": {
            },
            "limit": 10
        }
    }

    print('QUERYING BITDB')
    print(query_bitdb(query))

    print('QUERYING BITSOCKET')

    # query_bitsocket never returns so make sure your handler considers this
    def bitsocket_handler(j):
        print(j)

    query_bitsocket(query, bitsocket_handler)

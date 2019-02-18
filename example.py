#!/usr/bin/env python3

from bitdb import query_bitdb

print(query_bitdb({
    "v": 3,
    "q": {
        "find": {
        },
        "limit": 10
    }
}))


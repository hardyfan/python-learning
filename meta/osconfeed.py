import json
import os
import warnings
from urllib.request import urlopen


URL = "http://www.oreilly.com/pub/sc/osconfeed"
JSON = "data/osconfeed.json"


def load():
    if not os.path.exists(JSON):
        with urlopen(URL) as remote, open(JSON, "wb") as local:
            local.write(remote.read())
    with open(JSON, "rb") as fp:
        return json.load(fp)


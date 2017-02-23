#!/usr/bin/env python

import requests
import json

# For both Python 2 and Python 3
try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

def upload_from_url(url, path, token):
    if not path[-1] == '/':
        path += '/'
    # Getting file name from the url
    path += url.split('/')[-1]
    # Converting names to the appropriate format
    path, url = quote_plus(path), quote_plus(url)
    # Generating url for upload
    link = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path={}&url={}'
    link = link.format(path, url)
    headers = {'Authorization': 'OAuth {}'.format(token)}
    # Posting request
    r = requests.post(link, headers=headers)
    # Checking if everything is fine
    if '20' not in str(r.status_code):
        print('Something went wrong: ' + r.status_code)
    else:
        print('OK')

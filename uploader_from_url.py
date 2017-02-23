#!/usr/bin/env python

import requests
import json

# For both Python 2 and Python 3
try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

oauth = 'AQAAAAALbYSXAAMeSouRP3eE_0ZFlHJ3L_mgU1A'

def upload_from_url(url, token):
    # Getting file name from the url
    path = url.split('/')[-1]
    # Converting names to the apropriate format
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


upload_from_url('https://pp.vk.me/c626624/v626624016/49977/i4wGEHWzF4o.jpg', oauth)

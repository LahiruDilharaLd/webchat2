#!/usr/bin/env python
import requests
import sys

url = 'https://webchat.quakenet.org/'

if len(sys.argv) > 1:
    channel = sys.argv[1]
    url += '?channels=' + channel

response = requests.get(url)

if response.status_code == 200:
    print('Successfully connected to QuakeNet web chat.')
    print('URL:', response.url)
else:
    print('Failed to connect to QuakeNet web chat.')

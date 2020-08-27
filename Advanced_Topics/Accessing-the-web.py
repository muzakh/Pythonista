# -*- coding: utf-8 -*-
"""
Accessing the Web using urllib and HTTP lib modules
"""

import urllib
import urlopen
import sys


url = urllib.urlopen("http://www.fb.com")
for line in url:
    print(sys.stdout.write(line))


print("\n" * 2)

print(url.info())

print("\n" * 2)

##########################################################
'''  httplib module   '''
##########################################################


import httplib
webpages = ['index.html', '/doc/index.html']

web = httplib.HTTPConnection("www.python.org" , 80)

web.connect()

for page in webpages:
    req = web.request("GET", page)
    resp = web.getresponse()
    
    if resp.status == httplib.OK:
        data = resp.read()
        print("::::::::::::::::::::: {0} :::::::::::::::::::::" . format(page))
        print(data)

web.close()








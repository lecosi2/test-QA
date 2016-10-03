# -*- coding: utf-8 -*-
import requests

r = requests.get('http://asterisk.segurosdigitales.com:5000/')
status = r.status_code
print "STATUS =",status
if status == 200:
	print "Asterisk.segurosdigitales esta UP"
else:
    raise Exception ("se putio Asterisk por puerto 5000")
# -*- coding: utf-8 -*-
import requests

r = requests.get('http://www.mapfre.com.co/cotiautosws/ws?wsdl')
status = r.status_code
print "STATUS =",status
if status == 200 :
	print "MAPFRE esta UP"
else:
    raise Exception ("se putio mapfre")
# -*- coding: utf-8 -*-
import requests

r = requests.get('https://seguros.comparamejor.com/')
status = r.status_code
print "STATUS =",status
if status == 200 :
	print "segurosdigitales esta UP"
else:
    raise Exception ("se putio PAGINA WEB")
# -*- coding: utf-8 -*-
import requests

r = requests.get('https://www.cotizadoresgenerales.com/wsCotizaAutos/CotizaAutos.asmx?wsdl')
status = r.status_code
print ("STATUS =",status)
if status == 200 :
	print "AIG esta UP"
else:
    print ("<--> se putio AIG y que tales <-->")

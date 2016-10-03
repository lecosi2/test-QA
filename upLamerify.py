# -*- coding: utf-8 -*-
import requests

r = requests.get('http://74.207.233.137')
status = r.status_code
print "STATUS =",status
if status == 200 :
	print "---> LAMERIFY esta UP <---"

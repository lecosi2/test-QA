import requests

headers = {'Accept': 'application/json, text/plain, */*',
               'Accept-Encoding': 'gzip,deflate,sdch',
               'Accept-Language': 'es-ES,es;q=0.8,en;q=0.6',
               'Connection': 'keep-alive',
               'Host': 'api.suraenlinea.com',
               'Origin': 'https://www.suraenlinea.com',
               'Referer': 'https://www.suraenlinea.com/home',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_10) AppleWebKit/333.33 (KHTML, like Gecko) Chrome/33.0.9999.111 Safari/555.5',
    }

registration = "xcv234"
url = "https://api.suraenlinea.com/productos/autos/vehiculos/" + registration
res = requests.get(url, headers=headers)
print res
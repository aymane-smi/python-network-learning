#for linux
#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import json, http.client
from urllib.parse import quote_plus
def geocode(address):
	base = "/maps/api/geocode/json"
	path = "{}?address={}&sensor=false".format(base,quote_plus(address))
	connection = http.client.HTTPConnection('maps.google.com')
	connection.request('GET',path)
	reply = connection.getresponse()#.read()
	result = json.load(reply)#.decode('utf-8'))
	result = result['results'][0]['geometry']['location']
	result = str(result['lat'])+"/"+str(result['lng'])
	print(result)
if __name__ == '__main__':
	geocode("Avenue Mohamed Belkhadir, Safi")

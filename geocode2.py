#for linux
#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import requests
def geocode(address):
	parameters = {'address':address,'sensor':'false'}
	base = requests.get("https://maps.googleapis.com/maps/api/geocode/json",params=parameters)
	result = base.json()
  '''
  print(result)#in case if u want to see the full api code
  '''
	result = result["results"][0]["geometry"]["location"]
	result = str(result["lat"])+"/"+str(result['lng'])
	print(result)
if __name__ == '__main__':
	geocode("x")#x is the address

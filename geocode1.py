#use pip install pygeocoder or pypi to get pygeocoder model
from pygeocoder import Geocoder
result = Geocoder.geocode("x")#x is the address
print(result[0].coordinates)#print the coordinates of the address

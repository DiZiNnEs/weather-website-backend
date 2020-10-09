from django.contrib.gis.geoip2 import GeoIP2

g = GeoIP2()
g.country('google.com')

print(g)
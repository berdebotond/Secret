import urllib
import requests
#return the given websites's html
def scrap(url):
    weburl = request.urlopen(url)
    sourcecode = weburl.read()
    return sourcecode


google = scrap("https://google.com")
print(google)
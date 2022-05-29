import urllib.request
from bs4 import BeautifulSoup
#return the given websites's html
def scrap(url):
    weburl = urllib.request.urlopen(url)
    sourcecode = weburl.read()
    soup = BeautifulSoup(sourcecode)
    web_text = soup.get_text()
    no_line = web_text.split()
    done_txt = ''.join(no_line)
    return done_txt

google = scrap("https://en.wikipedia.org/wiki/The_Ghost_Islands")
print(google)
import urllib.request
from bs4 import BeautifulSoup
import csv
#return the given websites's html
def scrap(url):
    weburl = urllib.request.urlopen(url)
    sourcecode = weburl.read()
    soup = BeautifulSoup(sourcecode, features="html.parser")
    web_text = soup.get_text()
    no_line = web_text.split()
    done_txt = ''.join(no_line)
    return done_txt

text_done = scrap("https://en.wikipedia.org/wiki/The_Ghost_Islands")

def __read_data(self):
    # alphabet_only = text_done
    # ''.join(x for x in alphabet_only if x.isalpha())
    split_string = []
    n = 3
    for index in range(0, len(text_done), n):
        split_string.append(text_done[index:index + n])
    english = {
        'English' : split_string
        }
    with open('language_data.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(english.keys())
        writer.writerows(zip(*english.values()))

test = __read_data(text_done)
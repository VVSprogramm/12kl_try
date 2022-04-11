import requests
from bs4 import BeautifulSoup

lapa = requests.get("https://vvsprogramm.github.io/2021_debug/")

print(lapa)

saturs = BeautifulSoup(lapa.content, 'html.parser')

print(saturs.prettify())

print(list(saturs.children))
print([type(item)for item in list(saturs.children)])

html = list(saturs.children)[2]
print(list(html.children))

body = list(html.children)[3]
print(list(body.children))
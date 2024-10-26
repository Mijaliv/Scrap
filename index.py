from bs4 import BeautifulSoup
import requests

url = "https://ar.indeed.com"
seObtine = requests.get(url)
html_doc = seObtine.text

soup = BeautifulSoup(html_doc,"html.parser")

#titulo = soup.findAll("img")
#print(titulo)

#print(soup.prettify())

print(soup.html)

#print(soup.title)

#print(soup.p["class"])

#print(soup.get_text())

#print(soup.p)

#for i in soup.find_all("img"):
#    print(i.get("alt"))

#print(soup.fin("form"))
#print(soup.div["id"])
#print(soup.get_text())

#link = soup.a
from bs4 import BeautifulSoup
import requests
import re

url = 'https://ar.indeed.com/'
seObtine = requests.get(url)
html_doc = seObtine.text

soup = BeautifulSoup(html_doc,"html.parser")

#titulo = soup.findAll("img")
#print(titulo)

#print(soup.prettify())

#print(soup.html)

#print(soup.title)

#print(soup.)

#print(soup.p["class"])

#print(soup.get_text())

#print(soup.p)

#for i in soup.find_all('a'):
#    print(i.get('href'))

#print(soup.fin("form"))
#print(soup.div["id"])
#print(soup.get_text())

#link = soup.a

#print(soup.title.get_text)

#print(soup.head)

#for tag in soup.find_all(re.compile("cordoba")):
#    print(tag.name)

#print(soup.find_all('link'))

#print(soup.find_all("title"))
#soup.find_all(id="link2")

#for link in soup.find_all('a'):
#    print(link.get('href'))

#print(soup.get_text())
print(soup.find_all('title'))
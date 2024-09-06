from bs4 import BeautifulSoup
import requests

url = "https://www.unc.edu.ar/"
seObtine = requests.get(url)
html_doc = seObtine.text

soup = BeautifulSoup(html_doc,"html.parser")

titulo = soup.findAll("img")
print(titulo)

print(soup.prettify())

print(soup.html)

print(soup.title.name)

print(soup.p["class"])

print(soup.get_text())

print(soup.p)

for i in soup.find_all("img"):
    print(i.get("alt"))

print(soup.fin("form"))
print(soup.div["id"])
print(soup.get_text())

link = soup.a
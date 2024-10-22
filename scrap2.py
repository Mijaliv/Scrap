from urllib.error import URLError
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

from requests import HTTPError


def make_request(url, headers=None):
    request = Request(url, headers=headers or {})
    try:
       with urlopen(request, timeout=10) as response:
             print(response.status)
             return response.read(), response
    except HTTPError as error:
         print(error.status, error.reason)
    except URLError as error:
         print(error.reason)
    except TimeoutError:
         print("Request timed out")

def bajar(laDir): 
   laPag = urlopen(laDir) 
   return BeautifulSoup(laPag.read(),features="html.parser")


agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
url = "https://ar.computrabajo.com/"

body, response = make_request(
    url,
    {"User-Agent": agent}
)
 
realBody = body.decode("utf-8")
#print(body.decode("utf-8"))
#soup = BeautifulSoup(realBody)
soup = BeautifulSoup(realBody, features="lxml")



#print(soup.prettify())  # Para ver el HTML completo que estás recibiendo



ofertas = soup.find_all('h1', class_="title_page ")

if len(ofertas) > 0:
    print(ofertas[0].text)
else:
    print("No se encontraron ofertas.")

#print(soup.prettify())

#print(soup.title.string)

#print(soup.find_all('p'))


#print(soup.a['title'])#devuelve CompuTrabajo
#print(soup.a['alt'])
#print(soup.a)
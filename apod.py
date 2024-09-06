from urllib.request import urlopen 
from bs4 import BeautifulSoup


def bajar(laDir): 
   laPag = urlopen(laDir) 
   return BeautifulSoup(laPag.read())
   
def pone_cero(n):
#Función pavota que pasa un número a string con un cero adelante si es necesario
   if n < 10:
      return('0'+str(n))
   else:
      return(str(n))
   
def fecha_string (dia,mes,anio):
#Función que pasa una fecha a string
   return (str(anio) + pone_cero(mes) + pone_cero(dia))
   
def fecha_url (dia,mes,anio):
# El formato de los urls de las páginas de fotos del día se arma con la fecha así"""
   return('https://apod.nasa.gov/apod/ap' + fecha_string(dia,mes,anio) + '.html')

for dia in range(1,31):
#Bajamos cada página de abril de 2022 y: si mars aparece como palabra clave, imprimimos el url
#de la foto de ese día (y si no, no)"""
   sopa = bajar(fecha_url)(dia,4,22)
   keys = sopa.find('meta',{'name':'keywords'})
   if 'galaxy' in keys.attrs['content']:
      laimg = sopa.find('img').attrs['src']
      print(laimg)   
   

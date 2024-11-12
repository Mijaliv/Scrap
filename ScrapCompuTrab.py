import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError, Timeout

def make_request(url, headers=None):
    try:
        response = requests.get(url, headers=headers or {}, timeout=10)
        response.raise_for_status()
        print(response.status_code)
        return response.text
    except HTTPError as error:
        print(f"HTTP error: {error}")
    except Timeout:
        print("Request timed out")
    except Exception as error:
        print(f"Error: {error}")

def scrape_jobs(url, headers):
    html_content = make_request(url, headers)
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'lxml')
    
    jobs = []
    for job_elem in soup.find_all('article', class_='box_offer'):
        title_elem = job_elem.find('a', class_='js-o-link')
        title = title_elem.text.strip() if title_elem else 'No especificado'

        link = title_elem['href'] if title_elem else '#'
        full_link = f"https://ar.computrabajo.com{link}"

        location_elem = job_elem.find('p', class_='fs16 fc_base mt5')
        location = location_elem.text.strip() if location_elem else 'Ubicación no especificada'

        empresa_elem = job_elem.find('a', class_='fc_base t_ellipsis')
        empresa = empresa_elem.text.strip() if empresa_elem else 'Empresa no especificada'

        date_elem = job_elem.find('p', class_='fs13 fc_aux mt15')
        date = date_elem.text.strip() if date_elem else 'Fecha no especificada'

        salario_elem = job_elem.find('div', class_='fs13 mt15')
        salario = salario_elem.text.strip() if salario_elem else 'Salario no especificado'

        jornada_elem = job_elem.find('span', class_='dIB mr10')
        jornada = jornada_elem.text.strip() if jornada_elem else 'Jornada no especificada'
        
        # Agregar los detalles del empleo a la lista
        jobs.append({
            'title': title,
            'link': full_link,
            'location': location,
            'empresa': empresa,
            'date': date,
            'salario': salario,
            'jornada': jornada,
        })
    
    return jobs

# Definir el User-Agent
agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
url = "https://ar.computrabajo.com/trabajo-de-vendedor?p=2"

# Scrapeando los empleos
empleos = scrape_jobs(url, {"User-Agent": agent})

# Mostrar los resultados
for empleo in empleos:
    print(f"Título: {empleo['title']}")
    print(f"Enlace: {empleo['link']}")
    print(f"Ubicación: {empleo['location']}")
    print(f"Empresa: {empleo['empresa']}")
    print(f"Fecha de publicación: {empleo['date']}")
    print(f"Salario: {empleo['salario']}")
    print(f"Jornada: {empleo['jornada']}")
    print('---')

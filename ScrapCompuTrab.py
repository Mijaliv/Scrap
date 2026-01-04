import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError, Timeout
import json

def make_request(url, headers=None):
    try:
        response = requests.get(url, headers=headers or {}, timeout=10)
        response.raise_for_status()
        print(f"Conexión exitosa a {url} con estado: {response.status_code}")
        return response.text
    except HTTPError as error:
        print(f"Error HTTP: {error}")
    except Timeout:
        print("La petición ha caducado (timeout)")
    except Exception as error:
        print(f"Ocurrió un error: {error}")
    return None

def scrape_jobs(url, headers):
    html_content = make_request(url, headers)
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'lxml')
    
    jobs = []
    job_elements = soup.find_all('article', class_='box_offer')
    print(f"Se encontraron {len(job_elements)} ofertas de trabajo.")

    for job_elem in job_elements:
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

def save_to_json(data, filename):
    if not data:
        print("No se encontraron datos para guardar.")
        return
        
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Los datos se han guardado correctamente en {filename}")
    except IOError as e:
        print(f"Error al escribir en el archivo {filename}: {e}")

# --- Ejecución Principal ---
if __name__ == "__main__":
    # Definir el User-Agent para simular un navegador
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
    url = "https://ar.computrabajo.com/trabajo-de-vendedor?p=2"
    
    print("Iniciando scraping...")
    empleos = scrape_jobs(url, {"User-Agent": agent})
    
    # Guardar los resultados en un archivo JSON
    save_to_json(empleos, "computrabajo_jobs.json")

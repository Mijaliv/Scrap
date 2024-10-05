from bs4 import BeautifulSoup
import requests
import csv 

url = "https://ar.computrabajo.com/"
obtiene = requests.get(url)
html_doc= obtiene.text

soup = BeautifulSoup(html_doc, "html.parser")

careers_table = soup.find("table",{"class":"tabla_resultados"})
if careers_table:
    careers= careers_table.find_all("tr")[1:]
    with open("careers.csv","w",newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "University","Location"])
        for career in careers:
            columns = career.find_all("td")
            title = columns[0].text.strip()
            university = ""
            location = ""
            for column in columns:
                if "Universidad" in column.text:
                    university = column.text.strip()
                elif "Madrid" in column.text:
                    location = column.text.strip()
            writer.writerow([title,university,location])
else:
    print("No careers table found")


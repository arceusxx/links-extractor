import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

links = []

url = input("URL:\n")
while len(url) == 0:
    url = input("URL:\n")

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None:
            links.append(href)

except requests.exceptions.HTTPError as err:
    print(f"HTTP ERROR: {err}")
except requests.exceptions.RequestException as err:
    print(f"REQUEST ERROR: {err}")

if len(links) == 0:
    print("No link to extract.")
else:
    file_name = input("File name:\n")
    current_time = datetime.now().strftime("%H-%M-%S")
    if not file_name:
        file_name = f"links for {current_time}.csv"
    else:
        file_name = f"{file_name}.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Links'])
        for link in links:
            writer.writerow([link])

    print("Done.")

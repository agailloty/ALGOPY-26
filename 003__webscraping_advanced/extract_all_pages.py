import lxml
from lxml.html import fromstring
import pandas as pd
import os
from pathlib import Path

# Lire toutes les pages et à chaque fois exécuter les requêtes xpath pour récupérer les données

# Extraire la logique dans une fonction

"""
Lire une page html et convertir en xml
"""
def read_and_convert_page(page_path : str):
    page_content = ""
    with open(page_path, "r", encoding="utf-8") as file:
        page_content = file.read()
    return fromstring(page_content)

# tester avec la page 1

names = []
ages = []
values = []
wages = []

data_path = Path("data")
pages = os.listdir(data_path)


for page in pages: 
    xml_page =read_and_convert_page(data_path / page)
    page_names = xml_page.xpath('//a[starts-with(@href, "/player/") and @data-tippy-top="" and @aria-expanded="false"]/text()')
    names.append(page_names)
    page_ages = xml_page.xpath('//td[@class="d2" and @data-col="ae"]/text()')
    ages.append(page_ages)
    page_values = xml_page.xpath('//td[@class="d6" and @data-col="vl"]/text()')
    values.append(page_values)
    page_wages = xml_page.xpath('//td[@class="d6" and @data-col="wg"]/text()')
    wages.append(page_wages)


"""
data = {
    "names" : names,
    "ages" : ages,
    "values" : values,
    "wages" : wages
}

df = pd.DataFrame(data)

df.to_csv("data_extracted.csv", sep = ",")
"""
print(names)


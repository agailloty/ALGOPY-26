# Extraire le contenu des pages HTML en utilisant des requêtes Xpath

import lxml
from lxml.html import fromstring

# Lire page-1

page1 = ""

with open("data/sofifa-page-1.html", "r", encoding="utf-8") as file:
    page1 = file.read()

xml_page = fromstring(page1)

# names = xml_page.xpath("//a[starts-with(@href, '/player/') and @aria-expanded='false']/text()")

# ages = xml_page.xpath("//td[@class='d2' and @data-col='ae']/text()")

# teams = xml_page.xpath("//a[starts-with(@href, '/team/')]/text()")


# print(list(zip(names, ages, teams)))

players = xml_page.xpath('//a[starts-with(@href, "/player/") and @data-tippy-top="" and @aria-expanded="false"]/text()')
ages = xml_page.xpath('//td[@class="d2" and @data-col="ae"]/text()')
values = xml_page.xpath('//td[@class="d6" and @data-col="vl"]/text()')
wages = xml_page.xpath('//td[@class="d6" and @data-col="wg"]/text()')


#print(list(zip(players, ages)))

import pandas as pd

data = {
    "names" : players,
    "ages" : ages,
    "values" : values,
    "wages" : wages
}

df = pd.DataFrame(data)

df.to_csv("data_extracted.csv", sep = ",")


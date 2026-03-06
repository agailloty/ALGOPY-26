# Extraire le contenu des pages HTML en utilisant des requêtes Xpath

import lxml
from lxml.html import fromstring

# Lire page-1

page1 = ""

with open("data/sofifa-page-1.html", "r", encoding="utf-8") as file:
    page1 = file.read()

xml_page = fromstring(page1)

names = xml_page.xpath("//a[starts-with(@href, '/player/') and @aria-expanded='false']/text()")

ages = xml_page.xpath("//td[@class='d2' and @data-col='ae']/text()")

teams = xml_page.xpath("//a[starts-with(@href, '/team/')]/text()")


print(list(zip(names, ages, teams)))
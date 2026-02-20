# Guide Complet de la Syntaxe XPath pour Web Scraping

## 📌 Introduction

XPath est un langage de requête puissant pour naviguer et extraire des données dans les documents XML et HTML.

**Setup Python:**
```python
from lxml.html import fromstring

# Charger votre HTML (exemple avec un contenu string)
sofifa_xml = fromstring(sofifa)
```

---

## 1️⃣ Sélections Basiques

### 1.1 Sélectionner Tous les Éléments (Descendance Complète)

**XPath:**
```xpath
//tagname
```

**Description:** Sélectionne tous les éléments `tagname` peu importe où ils se trouvent dans le document.

**Python lxml:**
```python
# Récupérer tous les 'div'
all_divs = sofifa_xml.xpath('//div')

# Récupérer tous les 'a' (liens)
all_links = sofifa_xml.xpath('//a')

# Compter le nombre d'éléments
count = len(sofifa_xml.xpath('//p'))
print(f"Nombre de paragraphes: {count}")
```

---

### 1.2 Sélectionner les Enfants Directs

**XPath:**
```xpath
/parent/child
```

**Description:** Sélectionne uniquement les éléments `child` qui sont des enfants directs de `parent`.

**Python lxml:**
```python
# Tous les 'td' qui sont enfants directs de 'tr'
cells = sofifa_xml.xpath('//tr/td')

# Tous les 'li' enfants directs d'une 'ul'
list_items = sofifa_xml.xpath('//ul/li')

# Les 'span' enfants directs d'un 'div' avec class 'player-info'
spans_in_player = sofifa_xml.xpath('//div[@class="player-info"]/span')
```

---

### 1.3 Sélectionner l'Élément Racine

**XPath:**
```xpath
/html
```

**Description:** Sélectionne l'élément racine du document.

**Python lxml:**
```python
# Récupérer l'élément racine
root = sofifa_xml.xpath('/html')
print(root)  # Retourne une liste avec 1 élément

# Accéder directement à l'racine (plus simple)
root = sofifa_xml  # C'est déjà l'racine quand on utilise fromstring()
```

---

## 2️⃣ Sélection avec Attributs

### 2.1 Sélectionner par un Attribut Spécifique

**XPath:**
```xpath
//tagname[@attribute="value"]
```

**Description:** Sélectionne les éléments avec un attribut exact.

**Python lxml:**
```python
# Tous les 'div' avec class='player'
players = sofifa_xml.xpath('//div[@class="player"]')

# Tous les 'a' avec id='home-link'
home_link = sofifa_xml.xpath('//a[@id="home-link"]')

# Tous les 'img' avec alt='Player Photo'
photos = sofifa_xml.xpath('//img[@alt="Player Photo"]')

# Tous les input avec type='text'
text_inputs = sofifa_xml.xpath('//input[@type="text"]')
```

---

### 2.2 Sélectionner par Classe CSS

**XPath:**
```xpath
//tagname[@class="classname"]
```

**Description:** Sélectionne les éléments avec une classe CSS spécifique (match exact).

**Python lxml:**
```python
# Tous les 'tr' avec class='player-row'
player_rows = sofifa_xml.xpath('//tr[@class="player-row"]')

# Tous les 'span' avec class='rating'
ratings = sofifa_xml.xpath('//span[@class="rating"]')

# Élément avec plusieurs classes (match exact)
special = sofifa_xml.xpath('//div[@class="player highlight featured"]')
```

⚠️ **Important:** La classe doit correspondre EXACTEMENT. Si l'élément a d'autres classes, le sélecteur ne matchera pas.

---

### 2.3 Sélectionner par Attribut Contenant une Valeur

**XPath:**
```xpath
//tagname[contains(@attribute, "value")]
```

**Description:** Sélectionne les éléments où l'attribut CONTIENT la valeur (pas besoin d'être exact).

**Python lxml:**
```python
# Tous les 'a' dont href contient 'player'
player_links = sofifa_xml.xpath('//a[contains(@href, "player")]')

# Tous les 'div' dont la classe contient 'player'
player_divs = sofifa_xml.xpath('//div[contains(@class, "player")]')

# Plus flexible pour les classes multi-valeurs
highlighted = sofifa_xml.xpath('//div[contains(@class, "highlight")]')

# Liens externes (href contient http)
external_links = sofifa_xml.xpath('//a[contains(@href, "http")]')

# Tous les 'img' dont l'alt contient 'photo'
photos = sofifa_xml.xpath('//img[contains(@alt, "photo")]')
```

✅ **C'est la meilleure pratique** pour chercher par classe CSS en XPath.

---

### 2.4 Sélectionner par Attribut Commençant par une Valeur

**XPath:**
```xpath
//tagname[starts-with(@attribute, "value")]
```

**Description:** Sélectionne les éléments où l'attribut COMMENCE par la valeur.

**Python lxml:**
```python
# Tous les 'a' dont href commence par '/players'
internal_player_links = sofifa_xml.xpath('//a[starts-with(@href, "/players")]')

# Tous les 'img' dont src commence par '/assets'
local_images = sofifa_xml.xpath('//img[starts-with(@src, "/assets")]')

# Tous les 'div' dont l'id commence par 'player-'
player_elements = sofifa_xml.xpath('//div[starts-with(@id, "player-")]')
```

---

### 2.5 Sélectionner par Attribut Terminant par une Valeur

**XPath:**
```xpath
//tagname[ends-with(@attribute, "value")]
```

**Description:** Sélectionne les éléments où l'attribut SE TERMINE par la valeur.

**Python lxml:**
```python
# Tous les 'img' dont src se termine par '.jpg'
jpg_images = sofifa_xml.xpath('//img[ends-with(@src, ".jpg")]')

# Tous les 'a' dont href se termine par '.pdf'
pdf_links = sofifa_xml.xpath('//a[ends-with(@href, ".pdf")]')

# Tous les 'script' dont src se termine par '.min.js'
minified_scripts = sofifa_xml.xpath('//script[ends-with(@src, ".min.js")]')
```

---

### 2.6 Sélectionner les Éléments Possédant un Attribut

**XPath:**
```xpath
//tagname[@attribute]
```

**Description:** Sélectionne les éléments qui POSSÈDENT l'attribut (peu importe sa valeur).

**Python lxml:**
```python
# Tous les 'a' qui ont un attribut 'href' (tous les liens)
all_links = sofifa_xml.xpath('//a[@href]')

# Tous les 'img' qui ont un 'alt'
images_with_alt = sofifa_xml.xpath('//img[@alt]')

# Tous les 'div' qui ont un 'id'
elements_with_id = sofifa_xml.xpath('//div[@id]')

# Tous les 'input' qui ont un 'value'
inputs_with_value = sofifa_xml.xpath('//input[@value]')
```

---

### 2.7 Sélectionner les Éléments N'AYANT PAS un Attribut

**XPath:**
```xpath
//tagname[not(@attribute)]
```

**Description:** Sélectionne les éléments qui N'ONT PAS cet attribut.

**Python lxml:**
```python
# Tous les 'img' sans 'alt'
images_without_alt = sofifa_xml.xpath('//img[not(@alt)]')

# Tous les 'a' sans 'href'
invalid_links = sofifa_xml.xpath('//a[not(@href)]')

# Tous les 'div' sans 'class'
divs_without_class = sofifa_xml.xpath('//div[not(@class)]')
```

---

## 3️⃣ Prédicats et Indexation

### 3.1 Premier Élément

**XPath:**
```xpath
//tagname[1]
```

**Description:** Sélectionne le premier élément de type `tagname`.

**Python lxml:**
```python
# Premier 'tr' du document
first_row = sofifa_xml.xpath('//tr[1]')

# Premier 'div' avec class 'player'
first_player = sofifa_xml.xpath('//div[@class="player"][1]')

# Accéder au texte du premier élément
first_player_text = sofifa_xml.xpath('//div[@class="player"][1]/text()')
```

---

### 3.2 Dernier Élément

**XPath:**
```xpath
//tagname[last()]
```

**Description:** Sélectionne le dernier élément de type `tagname`.

**Python lxml:**
```python
# Dernier 'tr' du document
last_row = sofifa_xml.xpath('//tr[last()]')

# Dernier 'div' avec class 'player'
last_player = sofifa_xml.xpath('//div[@class="player"][last()]')

# Avant-dernier élément
before_last = sofifa_xml.xpath('//tr[last()-1]')
```

---

### 3.3 Position Spécifique

**XPath:**
```xpath
//tagname[position() = n]
```
ou simplement
```xpath
//tagname[n]
```

**Description:** Sélectionne l'élément à la position n.

**Python lxml:**
```python
# 3ème ligne du tableau
third_row = sofifa_xml.xpath('//tr[3]')

# 5ème joueur
fifth_player = sofifa_xml.xpath('//div[@class="player"][5]')

# 2ème cellule d'une ligne
second_cell = sofifa_xml.xpath('//tr/td[2]')

# Position spécifique avec condition
range_rows = sofifa_xml.xpath('//tr[position() > 5][position() < 10]')
```

---

### 3.4 Nombre d'Éléments

**XPath:**
```xpath
//tagname[count(...) = n]
```

**Description:** Sélectionne les éléments qui contiennent exactement n éléments enfants.

**Python lxml:**
```python
# 'tr' qui contiennent exactement 5 'td'
rows_with_5_cells = sofifa_xml.xpath('//tr[count(./td) = 5]')

# 'div' qui contiennent au moins 3 enfants 'span'
divs_with_many_spans = sofifa_xml.xpath('//div[count(./span) > 3]')

# Lignes avec plus de 2 cellules
long_rows = sofifa_xml.xpath('//tr[count(./td) > 2]')
```

---

## 4️⃣ Extraction de Texte

### 4.1 Extraire Tout le Texte

**XPath:**
```xpath
//tagname/text()
```

**Description:** Sélectionne le nœud texte direct de l'élément.

**Python lxml:**
```python
# Récupérer le texte du premier 'h1'
title_text = sofifa_xml.xpath('//h1/text()')
print(title_text)  # Retourne une liste: ['Mon Titre']

# Récupérer le texte du premier 'h1' (extraire le string)
title = sofifa_xml.xpath('//h1/text()')[0] if sofifa_xml.xpath('//h1/text()') else ""

# Tous les textes des 'td'
cell_texts = sofifa_xml.xpath('//td/text()')

# Texte d'un élément avec attribut spécifique
player_name = sofifa_xml.xpath('//span[@class="player-name"]/text()')
```

---

### 4.2 Extraire Tous les Textes (y compris les enfants)

**XPath:**
```xpath
//tagname//text()
```

**Description:** Sélectionne TOUS les nœuds texte, y compris ceux dans les éléments enfants.

**Python lxml:**
```python
# Tous les textes dans un 'div' avec class 'player'
player_content = sofifa_xml.xpath('//div[@class="player"]//text()')

# Concaténer tous les textes
full_text = ''.join(sofifa_xml.xpath('//div[@class="player"]//text()'))

# Avec strip pour nettoyer
texts = sofifa_xml.xpath('//div[@class="player"]//text()')
clean_texts = [text.strip() for text in texts if text.strip()]
```

---

### 4.3 Extraire le Texte d'un Élément Spécifique dans une Boucle

**XPath:**
```xpath
//tagname[condition]/text()
```

**Description:** Combine sélection d'éléments + extraction de texte.

**Python lxml:**
```python
# Texte de tous les 'span' avec class 'rating'
ratings = sofifa_xml.xpath('//span[@class="rating"]/text()')

# Texte du premier 'li' de chaque 'ul'
list_titles = sofifa_xml.xpath('//ul/li[1]/text()')

# Texte des 'a' contenant 'player' dans l'href
player_links_text = sofifa_xml.xpath('//a[contains(@href, "player")]/text()')

# Traiter le résultat pour une meilleure lisibilité
names = [name.strip() for name in sofifa_xml.xpath('//span[@class="player-name"]/text()')]
```

---

### 4.4 Extraire du Texte Contenant un Motif

**XPath:**
```xpath
//tagname[contains(text(), "motif")]
```

**Description:** Sélectionne les éléments dont le texte CONTIENT une chaîne spécifique.

**Python lxml:**
```python
# Tous les 'div' dont le texte contient 'Ronaldo'
ronaldo_elements = sofifa_xml.xpath('//div[contains(text(), "Ronaldo")]')

# Tous les 'li' dont le texte commence par 'A'
starting_with_a = sofifa_xml.xpath('//li[starts-with(text(), "A")]')

# Tous les 'p' dont le texte se termine par '.'
sentences = sofifa_xml.xpath('//p[ends-with(text(), ".")]')

# Extraire le texte
results = sofifa_xml.xpath('//p[contains(text(), "important")]//text()')
```

---

## 5️⃣ Navigation et Relations

### 5.1 Parent Directs

**XPath:**
```xpath
//tagname/..
```

**Description:** Sélectionne l'élément parent d'un élément.

**Python lxml:**
```python
# Obtenir le parent d'un 'span' avec class 'rating'
parent_of_rating = sofifa_xml.xpath('//span[@class="rating"]/..')

# Obtenir le parent d'un lien spécifique
parent_of_link = sofifa_xml.xpath('//a[@id="main-link"]/..')[0] if sofifa_xml.xpath('//a[@id="main-link"]/..') else None

# Naviguer plus haut: grand-parent
grandparent = sofifa_xml.xpath('//span[@class="rating"]/../../..')[0]
```

---

### 5.2 Frères et Sœurs (Sibling)

**XPath:**
```xpath
//tagname/following-sibling::tagname2
```

**Description:** Sélectionne les éléments frères qui viennent APRÈS.

**Python lxml:**
```python
# Tous les 'span' qui viennent après un 'span' avec class 'label'
following_spans = sofifa_xml.xpath('//span[@class="label"]/following-sibling::span')

# Les 'td' qui viennent après le premier 'td' dans une ligne
cells_after_first = sofifa_xml.xpath('//tr/td[1]/following-sibling::td')

# Tous les 'li' qui suivent un 'li' contenant 'Active'
items_after_active = sofifa_xml.xpath('//li[contains(text(), "Active")]/following-sibling::li')
```

---

### 5.3 Frères Précédents

**XPath:**
```xpath
//tagname/preceding-sibling::tagname2
```

**Description:** Sélectionne les éléments frères qui viennent AVANT.

**Python lxml:**
```python
# Tous les 'span' qui viennent avant un 'span' avec class 'value'
preceding_spans = sofifa_xml.xpath('//span[@class="value"]/preceding-sibling::span')

# Les 'td' qui viennent avant la dernière 'td' dans une ligne
cells_before_last = sofifa_xml.xpath('//tr/td[last()]/preceding-sibling::td')
```

---

### 5.4 Éléments Descendants

**XPath:**
```xpath
//tagname//descendant::tagname2
```

**Description:** Sélectionne TOUS les descendants (peu importe la profondeur).

**Python lxml:**
```python
# Tous les 'span' descendants d'un 'div' avec class 'player'
player_spans = sofifa_xml.xpath('//div[@class="player"]//span')

# Tous les 'a' descendants du body
all_links_in_body = sofifa_xml.xpath('//body//a')

# Tous les éléments avec un 'id' dans un 'div' parent
ids_in_div = sofifa_xml.xpath('//div[@id="content"]//*[@id]')
```

---

## 6️⃣ Wildcards et Sélections Générales

### 6.1 Tous les Éléments

**XPath:**
```xpath
//*
```

**Description:** Sélectionne TOUS les éléments du document.

**Python lxml:**
```python
# Tous les éléments du document
all_elements = sofifa_xml.xpath('//*')
print(f"Nombre total d'éléments: {len(all_elements)}")

# Tous les éléments avec une classe CSS
elements_with_class = sofifa_xml.xpath('//*[@class]')

# Tous les éléments avec un attribut 'data-*'
data_elements = sofifa_xml.xpath('//*[starts-with(@*, "data-")]')
```

---

### 6.2 Tous les Éléments Enfants

**XPath:**
```xpath
//tagname/*
```

**Description:** Sélectionne TOUS les enfants directs, peu importe le type.

**Python lxml:**
```python
# Tous les enfants directs d'une 'div'
all_children = sofifa_xml.xpath('//div[@id="content"]/*')

# Tous les enfants d'une 'ul' (les 'li')
list_items = sofifa_xml.xpath('//ul/*')

# Filtrer les enfants par type après récupération
div_children = sofifa_xml.xpath('//div[@id="container"]/*')
p_children = [el for el in div_children if el.tag == 'p']
```

---

### 6.3 Tous les Attributs d'un Élément

**XPath:**
```xpath
//tagname/@*
```

**Description:** Sélectionne TOUS les attributs d'un élément.

**Python lxml:**
```python
# Tous les attributs du premier 'div'
all_attrs = sofifa_xml.xpath('//div[1]/@*')

# Accéder aux attributs d'un élément
element = sofifa_xml.xpath('//div[@class="player"]')[0]
attributes = element.attrib  # Retourne un dictionnaire

# Boucler sur les attributs
for attr_name, attr_value in attributes.items():
    print(f"{attr_name}: {attr_value}")
```

---

## 7️⃣ Opérateurs Logiques

### 7.1 ET (and) - Toutes les Conditions

**XPath:**
```xpath
//tagname[@attr1="val1" and @attr2="val2"]
```

**Description:** Sélectionne les éléments qui respectent TOUTES les conditions.

**Python lxml:**
```python
# 'div' avec class 'player' ET id 'p123'
specific_player = sofifa_xml.xpath('//div[@class="player" and @id="p123"]')

# 'span' contenant 'rating' ET 'value'
ratings = sofifa_xml.xpath('//span[contains(@class, "rating") and contains(@class, "value")]')

# 'tr' avec plus de 5 'td' ET contenant 'Ronaldo'
rows = sofifa_xml.xpath('//tr[count(./td) > 5 and contains(., "Ronaldo")]')

# Plusieurs critères
players = sofifa_xml.xpath('//div[@class="player" and @data-position="ST" and @data-overall > 85]')
```

---

### 7.2 OU (or) - Au Moins Une Condition

**XPath:**
```xpath
//tagname[@attr1="val1" or @attr2="val2"]
```

**Description:** Sélectionne les éléments qui respectent AU MOINS une condition.

**Python lxml:**
```python
# 'span' avec class 'rating' OU class 'score'
elements = sofifa_xml.xpath('//span[@class="rating" or @class="score"]')

# 'a' pointant vers '/players' OU '/teams'
links = sofifa_xml.xpath('//a[starts-with(@href, "/players") or starts-with(@href, "/teams")]')

# Éléments avec id 'main' OU 'footer'
sections = sofifa_xml.xpath('//*[@id="main" or @id="footer"]')
```

---

### 7.3 NON (not)

**XPath:**
```xpath
//tagname[not(@attr="value")]
```

**Description:** Sélectionne les éléments qui NE respectent PAS la condition.

**Python lxml:**
```python
# 'div' sans class 'hidden'
visible_divs = sofifa_xml.xpath('//div[not(@class="hidden")]')

# 'a' dont href ne contient pas 'external'
internal_links = sofifa_xml.xpath('//a[not(contains(@href, "external"))]')

# Lignes sans class 'separator'
content_rows = sofifa_xml.xpath('//tr[not(@class="separator")]')

# Éléments avec texte mais pas vides
non_empty = sofifa_xml.xpath('//span[not(text()="") and text()]')
```

---

## 8️⃣ Comparateurs de Valeurs

### 8.1 Comparaison Numérique

**XPath:**
```xpath
//tagname[@data-attr > 50]
//tagname[@data-attr < 100]
//tagname[@data-attr >= 85]
```

**Description:** Comparaison de valeurs numériques.

**Python lxml:**
```python
# Position après le 5e élément
elements = sofifa_xml.xpath('//tr[position() > 5]')

# Longueur du texte > 50 caractères (dans certains XPath)
long_texts = sofifa_xml.xpath('//p[string-length(.) > 50]')

# Avec attributs numériques (si disponibles)
high_ratings = sofifa_xml.xpath('//div[@data-overall > 85]')

# Combiner avec contains
mid_range = sofifa_xml.xpath('//div[@data-rating >= 70 and @data-rating <= 90]')
```

---

### 8.2 Égalité et Différence

**XPath:**
```xpath
//tagname[@attr="exact"]
//tagname[@attr!="value"]
```

**Description:** Comparaison d'égalité/différence.

**Python lxml:**
```python
# Attribut égal exactement
exact_match = sofifa_xml.xpath('//div[@class="player"]')

# Pas égal (comparaison simple)
not_exact = sofifa_xml.xpath('//div[@id!="hidden"]')  # Note: != peut ne pas fonctionner

# Alternative pour "pas égal"
not_equal = sofifa_xml.xpath('//div[not(@id="hidden")]')
```

---

## 9️⃣ Fonctions XPath Utiles

### 9.1 String Functions - Longueur du Texte

**XPath:**
```xpath
//tagname[string-length(text()) > 10]
```

**Description:** Sélectionne les éléments dont le texte est plus long que N caractères.

**Python lxml:**
```python
# Textes plus longs que 20 caractères
long_texts = sofifa_xml.xpath('//p[string-length() > 20]')

# Textes courts (moins de 5 caractères)
short_texts = sofifa_xml.xpath('//span[string-length() < 5]')

# Titres avec texte entre 10 et 50 chars
good_titles = sofifa_xml.xpath('//h2[string-length() > 10 and string-length() < 50]')
```

---

### 9.2 Position et Count

**XPath:**
```xpath
//tagname[position() = 1]
//tagname[count(./child) = 5]
```

**Description:** Fonctions de position et de comptage.

**Python lxml:**
```python
# Premier élément
first = sofifa_xml.xpath('//tr[position() = 1]')

# Dernier élément (count total)
last = sofifa_xml.xpath('//tr[position() = last()]')

# Éléments avec exactement 3 'td'
specific_rows = sofifa_xml.xpath('//tr[count(./td) = 3]')

# Lignes avec plus de 2 enfants
multi_cells = sofifa_xml.xpath('//tr[count(./*) > 2]')
```

---

### 9.3 Substring - Extraction Partielle

**XPath:**
```xpath
//tagname[substring(@attr, 1, 5) = "value"]
```

**Description:** Extrait une partie d'une chaîne pour comparaison.

**Python lxml:**
```python
# Attribut commençant par 'user-' (5 premiers caractères)
user_attrs = sofifa_xml.xpath('//*[substring(@id, 1, 5) = "user-"]')

# Les 3 premiers caractères du texte égalent 'The'
starting_the = sofifa_xml.xpath('//p[substring(text(), 1, 3) = "The"]')

# Extraire les 5 derniers caractères de l'href
endings = sofifa_xml.xpath('//a[substring(@href, string-length(@href) - 4) = ".html"]')
```

---

### 9.4 Normalize-Space - Nettoyer les Espaces

**XPath:**
```xpath
//tagname[normalize-space() = "valeur"]
```

**Description:** Supprime les espaces inutiles pour comparaison.

**Python lxml:**
```python
# Texte exactement "Cristiano Ronaldo" (sans espaces supplémentaires)
exact_name = sofifa_xml.xpath('//span[normalize-space() = "Cristiano Ronaldo"]')

# Texte commençant par (après nettoyage)
starts_clean = sofifa_xml.xpath('//p[starts-with(normalize-space(), "The")]')

# Extraire et nettoyer le texte en Python
raw_texts = sofifa_xml.xpath('//span//text()')
clean_texts = [' '.join(text.split()) for text in raw_texts]  # Normalize spaces
```

---

### 9.5 Translate - Remplacement de Caractères

**XPath:**
```xpath
//tagname[contains(translate(@attr, "abc", "ABC"), "ABC")]
```

**Description:** Traduit/remplace des caractères.

**Python lxml:**
```python
# Cas-insensitif pour un attribut (convertir en majuscules)
case_insensitive = sofifa_xml.xpath('//div[contains(translate(@class, "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "PLAYER")]')

# C'est complexe, donc en Python c'est souvent plus simple:
divs_with_player = sofifa_xml.xpath('//div[contains(translate(@class, "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "PLAYER")]')

# Alternative Python simple
divs = sofifa_xml.xpath('//div[@class]')
player_divs = [d for d in divs if 'player' in d.get('class', '').lower()]
```

---

## 🔟 Alias d'Axes (Axes Abrégés)

### 10.1 Axes Courants

| Abrévié | Complet | Signification |
|---------|---------|---------------|
| `.` | `self::node` | L'élément courant |
| `..` | `parent::node` | Le parent |
| `@` | `attribute::` | Un attribut |
| `/tag` | `child::tag` | Enfant direct |
| `//tag` | `descendant-or-self::tag` | Descendant quelconque |
| `tag1/tag2` | `child::tag1/child::tag2` | Enfant puis enfant |

**Python lxml:**
```python
# Référence à l'élément courant
current = sofifa_xml.xpath('.')[0]  # Le document lui-même

# Parent
parent = sofifa_xml.xpath('//span[@class="rating"]/../..')[0] if sofifa_xml.xpath('//span[@class="rating"]/..') else None

# Attribut
hrefs = sofifa_xml.xpath('//a/@href')

# Enfants
children = sofifa_xml.xpath('//div[@id="content"]/ul/li')

# Descendants
all_spans = sofifa_xml.xpath('//div//span')
```

---

## 1️⃣1️⃣ Cas d'Usage Pratiques pour Sofifa

### Cas 1: Extraire les Noms et Overall des Joueurs

**XPath:**
```xpath
//tr[@class="player"]
```

**Python lxml:**
```python
# Supposons une structure HTML: <table><tr class="player"><td class="name">...</td>...</tr></table>
player_rows = sofifa_xml.xpath('//tr[@class="player"]')

players = []
for row in player_rows:
    name = row.xpath('.//td[@class="name"]/text()')[0] if row.xpath('.//td[@class="name"]/text()') else "N/A"
    overall = row.xpath('.//td[@class="overall"]/text()')[0] if row.xpath('.//td[@class="overall"]/text()') else "N/A"
    players.append({
        "name": name,
        "overall": overall
    })

print(players)
```

---

### Cas 2: Chercher un Joueur par Position

**XPath:**
```xpath
//tr[contains(.//td[@class="position"]/text(), "ST")]
```

**Python lxml:**
```python
# Tous les attaquants (Striker)
strikers = sofifa_xml.xpath('//tr[contains(.//td[@class="position"]/text(), "ST")]')

# Extraire les noms
striker_names = sofifa_xml.xpath('//tr[contains(.//td[@class="position"]/text(), "ST")]/td[@class="name"]/text()')

print(f"Strikers trouvés: {len(striker_names)}")
for name in striker_names:
    print(f"  - {name}")
```

---

### Cas 3: Joueurs avec Overall > 85

**XPath:**
```xpath
//tr[contains(.//td[@class="overall"]/text(), "8") or contains(.//td[@class="overall"]/text(), "9")]
```

**Python lxml:**
```python
# C'est complexe en XPath, plus facile en Python
all_players = sofifa_xml.xpath('//tr[@class="player"]')

top_players = []
for row in all_players:
    overall_text = row.xpath('.//td[@class="overall"]/text()')
    if overall_text:
        try:
            overall = int(overall_text[0])
            if overall > 85:
                name = row.xpath('.//td[@class="name"]/text()')[0]
                top_players.append({"name": name, "overall": overall})
        except ValueError:
            pass

print(f"Joueurs avec overall > 85: {top_players}")
```

---

### Cas 4: Extraire les Liens vers les Pages Détail

**XPath:**
```xpath
//tr[@class="player"]//a[contains(@href, "/player/")]/@href
```

**Python lxml:**
```python
# Tous les liens vers les pages de joueurs
player_urls = sofifa_xml.xpath('//tr[@class="player"]//a[contains(@href, "/player/")]/@href')

print(f"URLs de joueurs trouvées: {len(player_urls)}")
for url in player_urls[:5]:  # Afficher les 5 premières
    print(f"  - {url}")
```

---

### Cas 5: Vérifier si un Joueur Est dans un Club Spécifique

**XPath:**
```xpath
//tr[contains(.//td[@class="club"]/text(), "Real Madrid")]
```

**Python lxml:**
```python
# Tous les joueurs de Real Madrid
real_madrid_players = sofifa_xml.xpath('//tr[contains(.//td[@class="club"]/text(), "Real Madrid")]')

# Extraire les noms
player_names = sofifa_xml.xpath('//tr[contains(.//td[@class="club"]/text(), "Real Madrid")]/td[@class="name"]/text()')

print(f"Joueurs de Real Madrid: {len(player_names)}")
for name in player_names:
    print(f"  - {name}")
```

---

## 📚 Cheat Sheet Rapide

```python
from lxml.html import fromstring

# Charger HTML
sofifa_xml = fromstring(html_content)

# ===== BASIQUES =====
sofifa_xml.xpath('//div')                                    # Tous les div
sofifa_xml.xpath('//div[@class="player"]')                   # Div avec class précis
sofifa_xml.xpath('//div[contains(@class, "player")]')        # Div contenant "player"
sofifa_xml.xpath('//div[1]')                                 # Premier div
sofifa_xml.xpath('//div[last()]')                            # Dernier div

# ===== TEXTE =====
sofifa_xml.xpath('//div/text()')                             # Texte direct
sofifa_xml.xpath('//div//text()')                            # Tous les textes
sofifa_xml.xpath('//div[contains(text(), "Ronaldo")]')       # Si texte contient

# ===== ATTRIBUTS =====
sofifa_xml.xpath('//a/@href')                                # Tous les href
sofifa_xml.xpath('//span[@id]')                              # Tous les span avec id
sofifa_xml.xpath('//span[not(@id)]')                         # Tous les span sans id

# ===== NAVIGATION =====
sofifa_xml.xpath('//span/..').                               # Parent
sofifa_xml.xpath('//span/following-sibling::span')           # Frères après
sofifa_xml.xpath('//span/preceding-sibling::span')           # Frères avant

# ===== LOGIQUE =====
sofifa_xml.xpath('//div[@class="a" and @id="b"]')            # ET
sofifa_xml.xpath('//div[@class="a" or @class="b"]')          # OU
sofifa_xml.xpath('//div[not(@class="hidden")]')              # NOT

# ===== CHAINES =====
sofifa_xml.xpath('//a[starts-with(@href, "/")]')             # Commence par
sofifa_xml.xpath('//a[ends-with(@href, ".html")]')           # Finit par
sofifa_xml.xpath('//p[string-length() > 100]')               # Longueur > 100

# ===== COMPTAGE =====
sofifa_xml.xpath('//tr[count(./td) = 5]')                    # Exactement 5 td
sofifa_xml.xpath('//div[count(./*) > 3]')                    # Plus de 3 enfants
```

---

## 🚀 Conseils et Bonnes Pratiques

### ✅ À FAIRE:

1. **Tester votre XPath d'abord** dans une console/debugger
2. **Utiliser `contains()`** pour les classes CSS (plus robuste)
3. **Valider que la liste n'est pas vide** avant d'accéder à l'index [0]
4. **Nettoyer le texte** avec `.strip()` et `replace()`
5. **Gérer les erreurs** (KeyError, IndexError) avec try/except

### ❌ À ÉVITER:

1. **Ne pas utiliser `@class="exact"`** si la classe peut avoir d'autres valeurs
2. **Ne pas assumer** que la structure HTML ne change pas
3. **Ne pas faire trop de requêtes** sans délai
4. **Ne pas oublier** de gérer les exceptions quand on accède à [0]

### 🎯 Exemple Complet:

```python
from lxml.html import fromstring

sofifa_xml = fromstring(html_content)

def extract_players_xpath():
    """Exemples complets d'extraction avec XPath"""
    
    players = []
    
    # Récupérer toutes les lignes de joueurs
    rows = sofifa_xml.xpath('//tr[contains(@class, "player")]')
    
    for row in rows:
        try:
            # Utiliser des XPath relatifs (.) pour rester dans le contexte
            name = row.xpath('.//td[contains(@class, "name")]/a/text()')
            position = row.xpath('.//td[contains(@class, "position")]/text()')
            rating = row.xpath('.//td[contains(@class, "overall")]/text()')
            
            # Sécuriser l'accès
            name = name[0].strip() if name else "Unknown"
            position = position[0].strip() if position else "Unknown"
            rating = rating[0].strip() if rating else "0"
            
            players.append({
                "name": name,
                "position": position,
                "rating": rating
            })
        except Exception as e:
            print(f"Erreur lors de l'extraction: {e}")
            continue
    
    return players

# Utiliser la fonction
results = extract_players_xpath()
for player in results[:10]:  # Afficher les 10 premiers
    print(f"{player['name']} - {player['position']} ({player['rating']})")
```

---

## 📖 Ressources Complémentaires

- **W3Schools XPath**: https://www.w3schools.com/xml/xpath_intro.asp
- **Mozilla MDN XPath**: https://developer.mozilla.org/fr/docs/Web/XPath
- **lxml Documentation**: https://lxml.de/
- **Regex pour Python si XPath ne suffit pas**: https://docs.python.org/3/library/re.html

---

**Dernière mise à jour:** 2026-02-20

import requests

req = requests.get("https:/sofifa.com")

with open("gailloty.html", "w") as file:
    file.write(req.text)
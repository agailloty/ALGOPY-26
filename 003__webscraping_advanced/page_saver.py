# Script pour enregistrer les pages HTML en provenance de sofifa.com dans un dossier data

# J'utilise playwright codegen sofifa.com pour générer du script Python
# Que je vais adapter

import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import os
import pathlib


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sofifa.com/")

    page.get_by_role("button", name="Consent", exact=True).click()

    # Sélectionner deux colonnes supplémentaires : Height et Weight
    page.get_by_role("textbox", name="Add column").click()
    page.get_by_role("treeitem", name="Height").click()
    page.get_by_role("treeitem", name="Weight").click()
    page.get_by_role("main").filter(has_text="Columns selected AgeOverall").click()
    page.get_by_role("button", name="Apply").click()

    # Boucler pour sauvegarder les pages.

    # On aimerait qu'il crée le data data dans l'emplacement où se trouve le script

    base_directory = pathlib.Path(__file__).parent / "data"

    if not os.path.exists(base_directory):
        os.mkdir(base_directory)

    for i in range(5):
        filepath = base_directory / f"sofifa-page-{i+1}.html"
        time.sleep(2)
        with open(filepath, "w", encoding="utf-8") as file: # r : read ; w: write
            file.write(page.content())
        page.get_by_role("link", name="Next").click()
        time.sleep(2)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

# Script pour enregistrer les pages HTML en provenance de sofifa.com

# J'utilise playwright codegen sofifa.com pour générer du script Python
# Que je vais adapter

import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


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

    for i in range(5):
        with open(f"sofifa-page-{i+1}.html", "w", encoding="utf-8") as file: # r : read ; w: write
            file.write(page.content())
        page.get_by_role("link", name="Next").click()
        time.sleep(2)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

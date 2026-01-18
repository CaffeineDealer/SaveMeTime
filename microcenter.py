# Objective: Parse inventory information across different stores for any deals in microcenter 
# Created: Jan 18 2026
# Last Modified: Jan 18 2026
# Author: CaffeineDealer

# HTTP, expression matching, JSON
import requests
import re
import json

# Command line apps
import typer
app = typer.Typer()

def check_microcenter_stock(product_id):
    url = f"https://www.microcenter.com/product/{product_id}/hmm-coffee"

    # get the page
    response = requests.get(url)
    html = response.text

    # Find inventory data: search for a pattern
    match = re.search(r'var inventory = (\[.*?\])', html, re.DOTALL)

    if not match:
        print("No Inventory Data!")
        return
    
    # Parse JSON
    inventory = json.loads(match.group(1))
    print(f"Store Availability {product_id}:\n")
    inStock = [store for store in inventory if store['qoh'] > 0]
    
    if inStock:
        for store in inStock:
            print(f"{store['storeName']}: {store['qoh']} in stock")
    else:
        print("Out of Stock!")

@app.command()
def main(product_id: str):
    # product_id = input("Enter product ID: ")
    check_microcenter_stock(product_id)

if __name__ == "__main__":
    app()
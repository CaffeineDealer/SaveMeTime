

# Command line apps
import typer
app = typer.Typer()

from microcenter import check_microcenter_stock

@app.command()
def main(website, product_id):
    if website == "microcenter":
        check_microcenter_stock(product_id)

if __name__ == "__main__":
    app()
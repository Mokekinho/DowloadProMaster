import typer
from downloader import download_file
from monitor import view_monitor

app = typer.Typer()
url = "https://vjudge.net/contest/702787/problemPdf/A?descKey=2277087622002969"

@app.command()
def download():
    """Inicia o download do arquivo"""
    download_file(url)

@app.command()
def monitor():
    """Monitora o consumo de CPU e memória"""
    view_monitor() 


if __name__ == "__main__":
    app()
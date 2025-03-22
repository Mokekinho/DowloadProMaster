import typer
from downloader import download_file
from monitor import view_monitor

app = typer.Typer()

@app.command()
def download():
    """Inicia o download do arquivo"""
    download_file()

@app.command()
def monitor():
    """Monitora o consumo de CPU e memória"""
    view_monitor() 


if __name__ == "__main__":
    app()
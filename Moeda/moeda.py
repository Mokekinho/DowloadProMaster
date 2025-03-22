import requests
import typer
from loguru import logger
from datetime import timedelta

app = typer.Typer()
url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

logger.add("Moeda/api_requests.log", format="{time} | {level} | {message}", level="INFO", retention=timedelta(seconds=3))

try:
    requisicao = requests.get(url)

    if(requisicao.status_code == 404):
        logger.warning("Erro 404: Recurso não encontrado.")
    elif requisicao.status_code == 500:
        logger.warning("Erro 500: Problema no servidor.")

    elif(requisicao.status_code != 200):
        logger.warning(f"Erro inesperado: {requisicao.status_code}")
      
    

except requests.exceptions.RequestException as e: #guarda o valor de requests.exceptions.RequestException numa variavel qualquer, como "e"
    logger.error(f"Erro de conexão: {e}")
   


@app.command()
def dollar():
    print((f"R$ {float(requisicao.json()['USDBRL']['bid']):.2f}"))

@app.command()
def euro():
    print((f"R$ {float(requisicao.json()['EURBRL']['bid']):.2f}"))#€

@app.command()
def bitcoin():
    print((f"R$ {float(requisicao.json()['BTCBRL']['bid']):.2f}"))#₿




if __name__ == "__main__":
    app()
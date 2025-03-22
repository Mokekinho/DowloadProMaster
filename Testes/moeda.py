import requests
import typer
from loguru import logger

app = typer.Typer()
url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
logger.add("Testes/api_requests.log", format="{time} | {level} | {message}", level="INFO", retention="7 days")

try:
    logger.info("Iniciando a requisição de ")
    requisicao = requests.get(url)
    logger.warning("Erro 404: Recurso não encontrado.")

    if(requisicao.status_code == 404):
        print("❌ Erro 404: Recurso não encontrado.")
    elif requisicao.status_code == 500:
        print("💥 Erro 500: Problema no servidor.")
    
    elif(requisicao.status_code != 200):
        print(f"⚠️ Erro inesperado: {requisicao.status_code}")
    

except requests.exceptions.RequestException as e: #guarda o valor de requests.exceptions.RequestException numa variavel qualquer, como "e"
    print(f"Erro de conexão: {e}")


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
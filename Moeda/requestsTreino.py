import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") #criei uma variavel que guarda uma requisição,  essa reuisição da um get, (pega a ingormação em uma api).


print(requisicao) #isso vai retornar 200 OK, ou 404 Not foud.
print(requisicao.json())#isso vai informar os dados guardados no json. 
print(requisicao.status_code) #isso retorna o numero de for 200 é pq ta certo, util para testar em if

#requisicao2 = requests.post()

dicionario_requisicao = requisicao.json()


print("Dolar: " + dicionario_requisicao['USDBRL']['bid']) #acessando os campos do json
print("Euro: " + dicionario_requisicao['EURBRL']['bid'])
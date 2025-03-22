import typer

app = typer.Typer() #aqui eu to criando um objeto Typer para a minha aplicação, eu to entendendo que é como se eu tivesse criando um Scanner sc em Java, so que nesse caso pra fazer as coisas na linha de comando.

@app.command()#é um decorador que permite vc usar a função a baixo com o typer
def corinthians(): #Para criar um comando basta criar uma função como qualquer outra
    """Fala bem do corinthians"""
    print("O Corinthians é o maior do Brasil")

@app.command()
def bem(name: str, age: int):
    """Fala bem de alguem""" #Cria uma legenda pro comando
    print("O " +name+ " é lindo")
    print(f"O {name} Boonito")#string formatada que enm em kotlin
    print(f"O {name} tem {age} anos")

@app.command()
def podezoar(deve_zoar: bool = False): #esse argumento passa a ser opcional, tem como dar um --help para comandos
    if(deve_zoar):
        print("Pode zoar não")
    else:
        print("ai sim sabe das coisas")

if __name__ == "__main__": #assim que cria uma função main em python
    app() #To iniciano meu aplicativo.
import os
from datetime import datetime

#visto no video https://www.youtube.com/watch?v=tJxcKyFMTGo Ele tem uns videos sobre outras bibliotecas tambem
#video sobre os parte dois sobre ler e escrever em arquivos https://www.youtube.com/watch?v=Uh2ebFW8OYM&t=7s

print(dir(os))#segundo o mano é legal fazer isso com todos as bibliotecas que vc baixar ou for aprender
print(os.getcwd()) #pega o "current work directory"

os.chdir('/home/moises/Documents/VsCode')#chage directory
print(os.getcwd())

print(os.listdir())#lista os diretorios(é possivel passar o parametro de qual diretorio a gente quer lista, por padrao ele lista o atual, no caso a gente mudou para "/home/moises/Documents/VsCode")
os.chdir('DownloadManagerPro/Moeda')
          
print(os.listdir())

os.mkdir('TesteDePasta')#se eu fosse tentar fazer o codigo a baixo nao iria funcionar pois nao existe a pasta : TesteDePasta SE A PASTA JA EXISTIR DA ERRO
os.makedirs('TesteDePasta/testes')#ele consegue criar diretorios aninhados, ele recomenda usar so esse que é masi fácil.

os.rmdir('TesteDePasta') # da erro pq a pasta não esta vazia
os.removedirs('TesteDePasta/testes') #fazem o mesmo que o de cima so que pra remover ESSE È PERIGOSO

os.rename('mudoou.py', 'TesteDePasta/mudou.py' ) #renomeia a pasta

print(os.stat('TesteDePasta/mudou.py')) #mostra todos os satus como se fosse um json
print(os.stat('TesteDePasta/mudou.py').st_size) #mostra so o tamanho
print(os.stat('TesteDePasta/mudou.py').st_mtime) #mostra a hora da ultima motificação so que não da pra entender nada

mod_time = os.stat('TesteDePasta/mudou.py').st_mtime
print(datetime.fromtimestamp(mod_time)) #agora da pra entender a hora

for dirpath, dirnames, filenames in os.walk('/home/moises/Documents/VsCode'): #passa por todos os diretorios como se fosse uma arvore, é util pra procurar uma arquivo
    print('CurrentPath: ', dirpath)
    print('Directories:', dirnames)
    print('Files: ', filenames)
    print()

print(os.environ)#mostra todas as variaveis de ambiente
print()
print(os.environ.get('HOME')) #pega so o Home (/home/moises)

file_path = os.environ.get('HOME') + 'text.txt' #isso cria so a string, nao cria nenhuma negocio, so que o problema de criar arquivos a partir dessa string é a chance de a / estar no lugar errado
print(file_path)

file_path2 = os.path.join(os.environ.get('HOME'),'text.txt')#agora sim faz a junção de forma correta sem se preocupar com a /
print(file_path2)

with open(file_path2, 'w') as file: #agora sim o  arquivo vai ser criado e manipulado Desse jeito ele ta começando do inicio 
    #w -> modo escrita, r-> modo leitura -> a tudo, ai tem os binarios, mas ai é que enm em c
    file.write("Ola pessoal")

print(os.path.basename('tmp/issoai.txt')) #ele mostra o nome base do arquivo sem os diretorios,o arquivo não precisa de fato existir

print(os.path.dirname('/temp/teste/mudou.py')) #ele mostra só os diretorios sem o nome base 

print(os.path.split('/temp/teste/mudou.py')) # divide em base e diretorios(os diretorios ficam tudo junto )

print(os.path.exists('TesteDePasta/mudou.py')) #ve se o caminho existe ou não 
print(os.getcwd())

print(os.path.isdir('TesteDePasta/mudou.py')) #ve se é um diretorio, pelo oq eu eu vi o path tem outros is
print(os.path.isfile("TesteDePasta/mudou.py")) #ve se é um arquivo

print(os.path.splitext("TesteDePasta/mudou.py")) #divide o nome da extensão

print(dir(os.path)) #mostra todas as funções e coisas que eu posso usar de os.path, util para fazer bibliotecas pra ver se tem alguma função utli 


    


from loguru import logger


#Logs basicamente são informações do que esta acontecendo com o programa, isso é util para saber quando cada coisa foi feita, em programas de dowload isso é util para dizer ao usuario o que esta acontecendo e mostra sucesso ou erros.

#https://www.youtube.com/watch?v=y8qLhov8QU8 Video com mais detalhes sobre logs

logger.add("Testes/api_requests.log", format="{time} | {level} | {message}", level="INFO", retention="7 days") #cria um arquivo chamado api_requests.log, esse arquivo serve para guardar as informações do que esta acontecendo durante o programa., o campo "format"define o formato que as mesagens devem ser guardadas, o campo "level" define qual nivel é o mais baixo, o campo "rentention" define por quantos dias as mensagens seram guardadas no arquivo, isso faz com que o arquivo não fique enorme.
#Rentention não funcionou comigo, ver oq esta acontecendo de errado, agora funcionou, vai entender KKKKKKKKK
#as vezes o rentention funciona, as vezes não, pelo o que e entendi ele funciona so quando não é chamado nenhum logger, mas não da pra saber.


logger.info("Download iniciado")#para informações
logger.trace("Voce aceessou o serviço da Google")#mensagem de rastreio
logger.debug("Esta dando tudo certo")#mesagem de debug
logger.success("Download realizado com sucesso")#mensagem de suesso
logger.warning("Esse programa pode quebrar seu computador")#mensagem de aviso
logger.error("Não foi Possivel acessar a API")#mesagem de erro
logger.critical("Seu pc ta pegando fogo")#Mensagem criica


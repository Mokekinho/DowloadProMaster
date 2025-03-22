from loguru import logger


#Logs basicamente são informações do que esta acontecendo com o programa, isso é util para saber quando cada coisa foi feita, em programas de dowload isso é util para dizer ao usuario o que esta acontecendo e mostra sucesso ou erros.

#https://www.youtube.com/watch?v=y8qLhov8QU8 Video com mais detalhes sobre logs

logger.info("Download iniciado")#para informações
logger.trace("Voce asseçou o serviço da Google")#mensagem de rastreio
logger.debug("Esta dando tudo certo")#mesagem de debug
logger.success("Download realizado com sucesso")#mensagem de suesso
logger.warning("Esse programa pode quebrar seu computador")#mensagem de aviso
logger.error("Não foi Possivel acessar a API")#mesagem de erro
logger.critical("Seu pc ta pegando fogo")#Mensagem criica


from datetime import datetime

data_e_hora_atuais = datetime.now()
data_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')


def atualizaLog(texto, user):
  localLogs = '/home/mardonio/Documentos/DevPessoal/Programacao/Python/botFoster/logs/'
  arquivoPath = localLogs + user + ".txt" 
  arquivo = open(arquivoPath, "a")
  arquivo.writelines(data_em_texto + ' - ' + texto + '\n')
  arquivo.close()
  return True
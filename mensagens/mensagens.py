from urllib.request import urlopen
from json import loads

def get_frase_random():
  req = "https://allugofrases.herokuapp.com/frases/random"
  response = urlopen(req)
  obj = loads(response.read())
  mensagem = obj['frase'] + "\nLivro: " + obj['livro'] \
              + "\nAuthor: " + obj['autor']

  return mensagem

def get_cumprimento_message(msg):
  return 'Olá ' + msg.from_user.first_name + ', Legal poder falar com você'
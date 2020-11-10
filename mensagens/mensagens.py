from urllib.request import urlopen
from json import loads
import re


def get_frase_random():
    req = "https://allugofrases.herokuapp.com/frases/random"
    response = urlopen(req)
    obj = loads(response.read())
    mensagem = obj["frase"] + "\nLivro: " + obj["livro"] + "\nAuthor: " + obj["autor"]

    return mensagem


def get_cumprimento_message(msg):
    return "Olá " + msg.from_user.first_name + ", Legal poder falar com você"


def get_teste_message(msg):
    return "Olá " + msg.from_user.first_name + "\nEstou funcionando bem"


def get_contexto_frase(msg):
    text = msg.text
    if re.search("tudo bem", text, re.IGNORECASE) or re.search(
        "tudo bom", text, re.IGNORECASE
    ):
        return "Eu sou um bot, e estou funcionando bem obrigado\n E você como está?"
    elif re.search("estou bem", text, re.IGNORECASE):
        return (
            "Que bom!! em que posso lhe ajudar??"
            "\n escolha a opção /start caso tenha duvida do que posso fazer"
        )

    return 'Não entendi o que quis dizer com: \n\n"' + text + '"'

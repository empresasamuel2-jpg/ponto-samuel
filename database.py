import json
import os

from config import DATABASE
from utils import data_atual



def iniciar():

    pasta = os.path.dirname(DATABASE)


    if not os.path.exists(pasta):
        os.makedirs(pasta)


    if not os.path.exists(DATABASE):

        with open(
            DATABASE,
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                {},
                arquivo,
                indent=4
            )



def carregar():

    iniciar()

    with open(
        DATABASE,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)



def salvar(dados):

    with open(
        DATABASE,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            dados,
            arquivo,
            indent=4,
            ensure_ascii=False
        )



def registrar_horario(tipo, horario):

    dados = carregar()


    data = data_atual()

    chave = (
        f"{data[0]}-"
        f"{data[1]:02d}-"
        f"{data[2]:02d}"
    )


    if chave not in dados:

        dados[chave] = []


    dados[chave].append(
        {
            "tipo": tipo,
            "horario": horario
        }
    )


    salvar(dados)



def obter_registros_do_dia():

    dados = carregar()


    data = data_atual()


    chave = (
        f"{data[0]}-"
        f"{data[1]:02d}-"
        f"{data[2]:02d}"
    )


    return dados.get(
        chave,
        []
    )

import json
import os

from config import DATABASE


def iniciar():
    if not os.path.exists(DATABASE):
        with open(DATABASE, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4, ensure_ascii=False)


def carregar():
    iniciar()

    with open(DATABASE, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar(dados):
    with open(DATABASE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def obter_mes(ano, mes):
    dados = carregar()

    ano = str(ano)
    mes = f"{int(mes):02d}"

    if ano not in dados:
        dados[ano] = {}

    if mes not in dados[ano]:
        dados[ano][mes] = {}

    salvar(dados)

    return dados[ano][mes]


def registrar_horario(ano, mes, dia, campo, horario):
    dados = carregar()

    ano = str(ano)
    mes = f"{int(mes):02d}"
    dia = f"{int(dia):02d}"

    dados.setdefault(ano, {})
    dados[ano].setdefault(mes, {})
    dados[ano][mes].setdefault(dia, {})

    dados[ano][mes][dia][campo] = horario

    salvar(dados)


def obter_dia(ano, mes, dia):
    dados = carregar()

    ano = str(ano)
    mes = f"{int(mes):02d}"
    dia = f"{int(dia):02d}"

    return (
        dados
        .get(ano, {})
        .get(mes, {})
        .get(dia, {})
    )


def limpar_mes(ano, mes):
    dados = carregar()

    ano = str(ano)
    mes = f"{int(mes):02d}"

    if ano in dados and mes in dados[ano]:
        dados[ano][mes] = {}

    salvar(dados)

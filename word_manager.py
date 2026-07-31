import os
import shutil

from docx import Document

from config import (
    CURRENT_WORD,
    TEMP_FOLDER
)

from utils import (
    nome_arquivo
)



def preparar_pasta_temp():

    if not os.path.exists(TEMP_FOLDER):
        os.makedirs(TEMP_FOLDER)



def criar_copia_folha():

    preparar_pasta_temp()

    destino = os.path.join(
        TEMP_FOLDER,
        nome_arquivo()
    )

    shutil.copy(
        CURRENT_WORD,
        destino
    )

    return destino



def abrir_documento(caminho):

    documento = Document(
        caminho
    )

    return documento



def encontrar_tabela(documento):

    if not documento.tables:
        return None

    return documento.tables[0]



def preencher_celula(
        tabela,
        linha,
        coluna,
        valor
):

    try:

        tabela.cell(
            linha,
            coluna
        ).text = valor

    except Exception:

        pass



def preencher_registros(
        caminho,
        registros
):

    documento = abrir_documento(
        caminho
    )

    tabela = encontrar_tabela(
        documento
    )


    if tabela is None:

        documento.save(
            caminho
        )

        return caminho



    for registro in registros:

        tipo = registro["tipo"]

        horario = registro["horario"]



        if tipo == "entrada":

            preencher_celula(
                tabela,
                1,
                1,
                horario
            )


        elif tipo == "inicio":

            preencher_celula(
                tabela,
                1,
                2,
                horario
            )


        elif tipo == "fim":

            preencher_celula(
                tabela,
                1,
                3,
                horario
            )


        elif tipo == "saida":

            preencher_celula(
                tabela,
                1,
                4,
                horario
            )



    documento.save(
        caminho
    )


    return caminho



def gerar_folha(registros):

    arquivo = criar_copia_folha()


    preencher_registros(
        arquivo,
        registros
    )


    return arquivo



def verificar_modelo():

    return os.path.exists(
        CURRENT_WORD
    )

from docx import Document
from docx.shared import Pt
from copy import deepcopy
import os

from config import CURRENT_WORD, TEMP_FOLDER


class WordManager:

    def __init__(self):
        self.document = None
        self.table = None

    def abrir(self):
        self.document = Document(CURRENT_WORD)

        for tabela in self.document.tables:
            if len(tabela.rows) > 20:
                self.table = tabela
                break

        if self.table is None:
            raise Exception("Tabela da folha de ponto não encontrada.")

    def salvar(self, nome_arquivo):
        os.makedirs(TEMP_FOLDER, exist_ok=True)

        caminho = os.path.join(
            TEMP_FOLDER,
            nome_arquivo
        )

        self.document.save(caminho)

        return caminho

    def localizar_linha(self, dia):

        for row in self.table.rows:

            texto = row.cells[0].text.strip()

            if texto == f"{dia:02d}":
                return row

        return None

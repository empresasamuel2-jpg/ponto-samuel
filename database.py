import json
import os
from config import DATABASE

def iniciar():
    if not os.path.exists(DATABASE):
        with open(DATABASE, "w", encoding="utf8") as f:
            json.dump({}, f)

def carregar():
    iniciar()
    with open(DATABASE, "r", encoding="utf8") as f:
        return json.load(f)

def salvar(dados):
    with open(DATABASE, "w", encoding="utf8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

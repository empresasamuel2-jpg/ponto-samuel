import os

TOKEN = os.getenv("BOT_TOKEN")

DATA_FOLDER = "data"
TEMP_FOLDER = "temp"

CURRENT_WORD = os.path.join(DATA_FOLDER, "folha.docx")

DATABASE = os.path.join(DATA_FOLDER, "registros.json")

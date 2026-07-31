from datetime import datetime

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import TOKEN
from database import (
    registrar_horario,
    obter_dia,
)
from calculations import calcular_horasasync def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "👋 Bem-vindo ao Bot de Ponto!\n\n"
        "Comandos disponíveis:\n\n"
        "/entrada HH:MM\n"
        "/inicio HH:MM\n"
        "/fim HH:MM\n"
        "/saida HH:MM\n"
        "/hoje\n"
        "/folha\n"
        "/ajuda"
    )

    await update.message.reply_text(mensagem)


async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)def data_atual():
    agora = datetime.now()

    return (
        agora.year,
        agora.month,
        agora.day
    )

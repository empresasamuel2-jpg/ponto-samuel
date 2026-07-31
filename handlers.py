from datetime import datetime

from telegram import Update
from telegram.ext import ContextTypes

from database import (
    registrar_horario,
    obter_registros_do_dia,
)

from calculations import calcular_horas
from word_manager import gerar_folha


async def entrada(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Use assim:\n/entrada HH:MM"
        )
        return

    horario = context.args[0]

    registrar_horario(
        tipo="entrada",
        horario=horario
    )

    await update.message.reply_text(
        f"✅ Entrada registrada às {horario}"
    )



async def inicio(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Use assim:\n/inicio HH:MM"
        )
        return


    horario = context.args[0]

    registrar_horario(
        tipo="inicio",
        horario=horario
    )


    await update.message.reply_text(
        f"✅ Início do almoço registrado às {horario}"
    )



async def fim(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Use assim:\n/fim HH:MM"
        )
        return


    horario = context.args[0]


    registrar_horario(
        tipo="fim",
        horario=horario
    )


    await update.message.reply_text(
        f"✅ Retorno registrado às {horario}"
    )



async def saida(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Use assim:\n/saida HH:MM"
        )
        return


    horario = context.args[0]


    registrar_horario(
        tipo="saida",
        horario=horario
    )


    await update.message.reply_text(
        f"✅ Saída registrada às {horario}"
    )



async def hoje(update: Update, context: ContextTypes.DEFAULT_TYPE):

    registros = obter_registros_do_dia()


    if not registros:
        await update.message.reply_text(
            "Nenhum registro encontrado hoje."
        )
        return


    texto = "📅 Registros de hoje:\n\n"


    for item in registros:
        texto += (
            f"{item['tipo'].upper()}: "
            f"{item['horario']}\n"
        )


    total = calcular_horas(registros)


    texto += (
        f"\n⏱ Total trabalhado: {total}"
    )


    await update.message.reply_text(texto)




async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = """
📌 COMANDOS DO BOT DE PONTO

/entrada HH:MM
Registra início do trabalho

/inicio HH:MM
Saída para almoço

/fim HH:MM
Retorno do almoço

/saida HH:MM
Finaliza expediente

/hoje
Mostra registros do dia

/folha
Gera folha de ponto

"""

    await update.message.reply_text(texto)



async def folha(update: Update, context: ContextTypes.DEFAULT_TYPE):

    registros = obter_registros_do_dia()


    if not registros:

        await update.message.reply_text(
            "Nenhum registro encontrado hoje."
        )

        return


    arquivo = gerar_folha(
        registros
    )


    await update.message.reply_document(
        document=open(
            arquivo,
            "rb"
        ),
        filename="folha.docx"
    )

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Bot de Ponto iniciado com sucesso!\n\n"
        "Comandos disponíveis:\n"
        "/start\n"
        "/ajuda"
    )


async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Em desenvolvimento.\n"
        "Em breve estarão disponíveis os comandos de registro de ponto."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ajuda", ajuda))

    print("Bot iniciado...")

    app.run_polling()


if __name__ == "__main__":
    main()

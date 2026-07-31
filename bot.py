from telegram.ext import (
    Application,
    CommandHandler
)

from config import TOKEN

from handlers import (
    entrada,
    inicio,
    fim,
    saida,
    hoje,
    ajuda
)



def main():

    app = Application.builder().token(TOKEN).build()


    app.add_handler(
        CommandHandler(
            "entrada",
            entrada
        )
    )


    app.add_handler(
        CommandHandler(
            "inicio",
            inicio
        )
    )


    app.add_handler(
        CommandHandler(
            "fim",
            fim
        )
    )


    app.add_handler(
        CommandHandler(
            "saida",
            saida
        )
    )


    app.add_handler(
        CommandHandler(
            "hoje",
            hoje
        )
    )


    app.add_handler(
        CommandHandler(
            "ajuda",
            ajuda
        )
    )


    print(
        "🤖 Bot de ponto iniciado..."
    )


    app.run_polling()



if __name__ == "__main__":
    main()

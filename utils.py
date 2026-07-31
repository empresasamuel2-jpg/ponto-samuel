from datetime import datetime


def data_atual():

    agora = datetime.now()

    return (
        agora.year,
        agora.month,
        agora.day
    )



def horario_atual():

    agora = datetime.now()

    return agora.strftime("%H:%M")



def nome_arquivo():

    ano, mes, dia = data_atual()

    return (
        f"folha_{dia:02d}_"
        f"{mes:02d}_"
        f"{ano}.docx"
    )



def formatar_data():

    ano, mes, dia = data_atual()

    return (
        f"{dia:02d}/"
        f"{mes:02d}/"
        f"{ano}"
    )

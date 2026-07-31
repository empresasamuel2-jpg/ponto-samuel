from datetime import datetime



def converter_hora(hora):

    return datetime.strptime(
        hora,
        "%H:%M"
    )



def calcular_horas(registros):

    entrada = None
    inicio = None
    fim = None
    saida = None


    for registro in registros:

        tipo = registro["tipo"]
        horario = registro["horario"]


        if tipo == "entrada":
            entrada = horario


        elif tipo == "inicio":
            inicio = horario


        elif tipo == "fim":
            fim = horario


        elif tipo == "saida":
            saida = horario



    if not entrada or not saida:

        return "Expediente incompleto"



    inicio_trabalho = converter_hora(
        entrada
    )


    fim_trabalho = converter_hora(
        saida
    )


    total = (
        fim_trabalho -
        inicio_trabalho
    )


    if inicio and fim:

        pausa = (
            converter_hora(fim)
            -
            converter_hora(inicio)
        )

        total -= pausa



    horas = total.seconds // 3600

    minutos = (
        total.seconds % 3600
    ) // 60


    return (
        f"{horas:02d}:"
        f"{minutos:02d}"
    )

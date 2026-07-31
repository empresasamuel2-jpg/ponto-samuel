from datetime import datetime, timedelta


def converter_hora(hora):
    """
    Converte uma string no formato HH:MM para um objeto datetime.
    """
    return datetime.strptime(hora, "%H:%M")


def calcular_horas(entrada, saida, intervalo_inicio=None, intervalo_fim=None):
    """
    Calcula as horas trabalhadas.

    entrada: "07:50"
    saida: "17:30"
    intervalo_inicio: "12:00" (opcional)
    intervalo_fim: "13:00" (opcional)
    """

    entrada = converter_hora(entrada)
    saida = converter_hora(saida)

    # Caso passe da meia-noite
    if saida < entrada:
        saida += timedelta(days=1)

    total = saida - entrada

    if intervalo_inicio and intervalo_fim:
        inicio = converter_hora(intervalo_inicio)
        fim = converter_hora(intervalo_fim)

        if fim < inicio:
            fim += timedelta(days=1)

        total -= (fim - inicio)

    horas = total.seconds // 3600
    minutos = (total.seconds % 3600) // 60

    return f"{horas:02d}:{minutos:02d}"

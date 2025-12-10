import sys
from collections import Counter


def get_dados_modal(resultados, tipo):
    dados = Counter(resultados)

    if not dados:
        return 0, 0

    max_freq = max(dados.values())
    modas = [value for value, freq in dados.items() if freq == max_freq]

    if tipo == "min":
        valor_modal = min(modas)
    elif tipo == "max":
        valor_modal = max(modas)
    else:
        valor_modal = modas[0]

    return valor_modal, max_freq


def print_com_flush(msg):
    sys.stdout.write("\r" + msg + f"{' ' * 5}")
    sys.stdout.flush()

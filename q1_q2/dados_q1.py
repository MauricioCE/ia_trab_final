import numpy as np


def func_obj_1(x1, x2):
    return x1**2 + x2**2


def func_obj_2(x1, x2):
    term1 = np.exp(-(x1**2 + x2**2))
    term2 = 2 * np.exp(-((x1 - 1.7) ** 2 + (x2 - 1.7) ** 2))
    return term1 + term2


def func_obj_3(x1, x2):
    termo_raiz = -0.2 * np.sqrt(0.5 * (x1**2 + x2**2))
    termo_cos = 0.5 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))
    return -20 * np.exp(termo_raiz) - np.exp(termo_cos) + 20 + np.exp(1)


def func_obj_4(x1, x2):
    termo_x1 = x1**2 - 10 * np.cos(2 * np.pi * x1) + 10
    termo_x2 = x2**2 - 10 * np.cos(2 * np.pi * x2) + 10
    return termo_x1 + termo_x2


def func_obj_5(x1, x2):
    term1 = (x1 * np.cos(x1)) / 20
    term2 = 2 * np.exp(-(x1**2) - (x2 - 1) ** 2)
    term3 = 0.01 * x1 * x2
    return term1 + term2 + term3


def func_obj_6(x1, x2):
    return x1 * np.sin(4 * np.pi * x1) - x2 * np.sin(4 * np.pi * x2 + np.pi) + 1


MAX_RODADAS = 100
MAX_INTERACOES = 1000
MAX_INTERACOES_SEM_MELHORIA = 500
MAX_VIZINHOS = 20
PRECISAO_DECIMAL = 4


dados_q1 = [
    ("Q1", func_obj_1, [(-100.0, 100.0), (-100.0, 100.0)], "min", 0.5, 0.5),
    ("Q2", func_obj_2, [(-2.0, 4.0), (-2.0, 5.0)], "max", 0.1, 0.1),
    ("Q3", func_obj_3, [(-8.0, 8.0), (-8.0, 8.0)], "min", 0.1, 0.1),
    ("Q4", func_obj_4, [(-5.12, 5.12), (-5.12, 5.12)], "min", 0.1, 0.1),
    ("Q5", func_obj_5, [(-10.0, 10.0), (-10.0, 10.0)], "max", 0.1, 0.1),
    ("Q6", func_obj_6, [(-1.0, 3.0), (-1.0, 3.0)], "max", 0.1, 0.1),
]

from hill_clibing import HillClimbing
from lrs import LRS
from grs import GRS
from dados_q1 import dados_q1
from ts import TS
import pandas as pd


# ==============================  QUESTÃO 01  ==============================

hc = HillClimbing()
lrs = LRS()
grs = GRS()

resultados_hc = hc.execute(dados_q1)
resultados_lrs = lrs.execute(dados_q1)
resultados_grs = grs.execute(dados_q1)

dados = [
    # --- HILL CLIMBING (HC) ---
    {
        "Algoritmo": "Hill Climbing Q1",
        "f best": resultados_hc["Q1"][0],
        "freq": resultados_hc["Q1"][1],
    },
    {
        "Algoritmo": "Hill Climbing Q2",
        "f best": resultados_hc["Q2"][0],
        "freq": resultados_hc["Q2"][1],
    },
    {
        "Algoritmo": "Hill Climbing Q3",
        "f best": resultados_hc["Q3"][0],
        "freq": resultados_hc["Q3"][1],
    },
    {
        "Algoritmo": "Hill Climbing Q4",
        "f best": resultados_hc["Q4"][0],
        "freq": resultados_hc["Q4"][1],
    },
    {
        "Algoritmo": "Hill Climbing Q5",
        "f best": resultados_hc["Q5"][0],
        "freq": resultados_hc["Q5"][1],
    },
    {
        "Algoritmo": "Hill Climbing Q6",
        "f best": resultados_hc["Q6"][0],
        "freq": resultados_hc["Q6"][1],
    },
    # --- LOCAL RANDOM SEARCH (LRS) ---
    {
        "Algoritmo": "Local Random Search Q1",
        "f best": resultados_lrs["Q1"][0],
        "freq": resultados_lrs["Q1"][1],
    },
    {
        "Algoritmo": "Local Random Search Q2",
        "f best": resultados_lrs["Q2"][0],
        "freq": resultados_lrs["Q2"][1],
    },
    {
        "Algoritmo": "Local Random Search Q3",
        "f best": resultados_lrs["Q3"][0],
        "freq": resultados_lrs["Q3"][1],
    },
    {
        "Algoritmo": "Local Random Search Q4",
        "f best": resultados_lrs["Q4"][0],
        "freq": resultados_lrs["Q4"][1],
    },
    {
        "Algoritmo": "Local Random Search Q5",
        "f best": resultados_lrs["Q5"][0],
        "freq": resultados_lrs["Q5"][1],
    },
    {
        "Algoritmo": "Local Random Search Q6",
        "f best": resultados_lrs["Q6"][0],
        "freq": resultados_lrs["Q6"][1],
    },
    # --- GLOBAL RANDOM SEARCH (GRS) ---
    {
        "Algoritmo": "Global Random Search Q1",
        "f best": resultados_grs["Q1"][0],
        "freq": resultados_grs["Q1"][1],
    },
    {
        "Algoritmo": "Global Random Search Q2",
        "f best": resultados_grs["Q2"][0],
        "freq": resultados_grs["Q2"][1],
    },
    {
        "Algoritmo": "Global Random Search Q3",
        "f best": resultados_grs["Q3"][0],
        "freq": resultados_grs["Q3"][1],
    },
    {
        "Algoritmo": "Global Random Search Q4",
        "f best": resultados_grs["Q4"][0],
        "freq": resultados_grs["Q4"][1],
    },
    {
        "Algoritmo": "Global Random Search Q5",
        "f best": resultados_grs["Q5"][0],
        "freq": resultados_grs["Q5"][1],
    },
    {
        "Algoritmo": "Global Random Search Q6",
        "f best": resultados_grs["Q6"][0],
        "freq": resultados_grs["Q6"][1],
    },
]

df_dicionario = pd.DataFrame(dados)
print(f"\n{df_dicionario.to_markdown(index=False)}")
br = 1


# ==============================  QUESTÃO 02  ==============================


# ts = TS()

# print("Executando TS sem vizinhança controlada\n")
# resultados_ts = ts.execute(achar_todas=True, usar_vizinhanca_controlada=False)

# print("\n\n")

# print("Executando TS com vizinhança controlada\n")
# resultados_ts = ts.execute(achar_todas=True, usar_vizinhanca_controlada=True)

# br = 1

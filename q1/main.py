from hill_clibing import HillClimbing
from lrs import LRS
from grs import GRS
from dados import dados_q1
from helper import get_dados_modal


# *****  FUNÇÃO DE AJUDA PARA CALCULAR A MODA  *****

hc = HillClimbing()
lrs = LRS()
grs = GRS()

# resultados_hc = hc.execute(dados_q1)
# resultados_lrs = lrs.execute(dados_q1)
resultados_grs = grs.execute(dados_q1)

# valor_6, freq_6 = get_dados_modal(r_hc_6)
# valor_1, freq_1 = get_dados_modal(r_lrs_1)
valor_grs, freq_grs = get_dados_modal(resultados_grs)

br = 1

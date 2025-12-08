import numpy as np
from dados import (
    MAX_RODADAS,
    MAX_INTERACOES,
    MAX_INTERACOES_SEM_MELHORIA,
    PRECISAO_DECIMAL,
)
import helper


class GRS:
    def execute(self, dados):
        resultados = []

        for id, func_obj, limites, tipo, _, _ in dados:
            resultados.append(
                self._search(id, func_obj, limites, tipo, MAX_RODADAS, log=True)
            )

        return resultados

    def _search(self, id, func_obj, limites, tipo, rodadas, log=False):
        solucoes = []

        limites_inf = np.array([b[0] for b in limites])
        limites_sup = np.array([b[1] for b in limites])
        dim = len(limites)

        for rodada in range(1, rodadas + 1):
            x_best = np.random.uniform(low=limites_inf, high=limites_sup, size=dim)
            f_best = func_obj(*x_best)

            interacoes = 1
            interacoes_sem_melhoria = 0

            while (
                interacoes <= MAX_INTERACOES
                and interacoes_sem_melhoria <= MAX_INTERACOES_SEM_MELHORIA
            ):
                melhoria = False

                x_cand = np.random.uniform(low=limites_inf, high=limites_sup, size=dim)
                f_cand = func_obj(*x_cand)

                helper.print_com_flush(
                    f"GRS: {id} - Rodada {rodada} - Interação {interacoes:02d}"
                )

                interacoes += 1
                if (tipo == "max" and f_cand > f_best) or (
                    tipo == "min" and f_cand < f_best
                ):
                    melhoria = True
                    x_best = x_cand
                    f_best = f_cand
                    interacoes_sem_melhoria = 0

                if not melhoria:
                    interacoes_sem_melhoria += 1

            f_best = np.round(f_best, PRECISAO_DECIMAL)
            solucoes.append(f_best)
        print()

        return helper.get_dados_modal(solucoes)

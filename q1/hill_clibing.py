import numpy as np
import matplotlib.pyplot as plt
import helper
from dados import (
    MAX_RODADAS,
    MAX_INTERACOES,
    MAX_INTERACOES_SEM_MELHORIA,
    MAX_VIZINHOS,
    PRECISAO_DECIMAL,
)


class HillClimbing:
    def execute(self, dados):
        resultados = []

        for id, func_obj, limites, tipo, episilon, _ in dados:
            resultados.append(
                self.climb(func_obj, limites, tipo, MAX_RODADAS, episilon, id)
            )

        return resultados

    def climb(
        self,
        func_obj,
        limites,
        tipo,
        rodadas,
        epsilon,
        id,
    ):
        solucoes = []

        # só para mostrar o gráfico
        x_coords = []
        y_coords = []
        f_coords = []

        for rodada in range(1, rodadas + 1):
            x_best_lista = []
            x_best_lista.append(limites[0][0])
            x_best_lista.append(limites[1][0])

            limites_inf = np.array([b[0] for b in limites])
            limites_sup = np.array([b[1] for b in limites])

            x_best = np.array(x_best_lista)
            f_best = func_obj(*x_best)

            interacoes = 0
            interacoes_sem_melhoria = 0

            while (
                interacoes <= MAX_INTERACOES
                and interacoes_sem_melhoria <= MAX_INTERACOES_SEM_MELHORIA
            ):
                melhoria = False
                interacoes += 1
                vizinhos = 1

                while vizinhos <= MAX_VIZINHOS:
                    x_cand = np.random.uniform(
                        low=x_best - epsilon, high=x_best + epsilon
                    )

                    x_cand = np.clip(x_cand, limites_inf, limites_sup)
                    f_cand = func_obj(*x_cand)

                    helper.print_com_flush(
                        f"HC : {id} - Rodada {rodada} - Interação {interacoes:02d} - Vizinho {vizinhos:02d}"
                    )

                    vizinhos += 1

                    if (tipo == "max" and f_cand > f_best) or (
                        tipo == "min" and f_cand < f_best
                    ):
                        melhoria = True
                        x_best = x_cand
                        f_best = f_cand
                        interacoes_sem_melhoria = 0
                        break

                if not melhoria:
                    interacoes_sem_melhoria += 1
            f_best = np.round(f_best, PRECISAO_DECIMAL)
            solucoes.append(f_best)
            x_coords.append(x_best[0])
            y_coords.append(x_best[1])
            f_coords.append(f_best)

        # grafico(x_coords, y_coords, f_coords, func_obj)
        print()
        return helper.get_dados_modal(solucoes)


def grafico(x_coords, y_coords, f_coords, func_obj):
    lim_inf = -100
    lim_sup = 100
    x_axis = np.linspace(lim_inf, lim_sup, 500)
    X, Y = np.meshgrid(x_axis, x_axis)
    fig = plt.figure(1)
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(
        X, Y, func_obj([X, Y]), rstride=30, cstride=30, alpha=0.1, edgecolors="k"
    )
    ax.scatter(
        x_coords,
        y_coords,
        f_coords,
        s=30,
        marker="o",
        c=f_coords,
        cmap="plasma",
        label="Pontos de Solução Coletados",
    )

    plt.pause(1)
    plt.show()

import numpy as np
import helper as helper
import time


MAX_RODADAS = 100
MAX_INTERACOES = 1000
PRECISAO_DECIMAL = 4
TEMPERATURA_INICIAL = 10
FATOR_RESFRIAMENTO = 0.99

# Objetivo: maximizar f(x) = 28 - h(x)
# h(x) = número de pares de rainhas atacantes


class TS:
    def h(self, board):
        attacks = 0
        n = len(board)

        for i in range(n):
            for j in range(i + 1, n):
                if board[i] == board[j]:
                    attacks += 1

                if abs(board[i] - board[j]) == abs(i - j):
                    attacks += 1

        return attacks

    def func(self, x):
        return 28 - self.h(x)

    def get_vizinho_controlado(self, x_atual):
        lim_inf = 0
        lim_sup = 7
        dim = 8
        x_cand = x_atual.copy()
        direcao = np.random.choice([-1, 1])
        col = np.random.randint(0, dim)
        nova_linha = x_cand[col] + direcao

        if lim_inf <= nova_linha <= lim_sup:
            x_cand[col] = nova_linha
            return x_cand
        else:
            nova_linha = x_atual[col] - direcao
            if lim_inf <= nova_linha <= lim_sup:
                x_cand[col] = nova_linha
                return x_cand
            else:
                return x_atual

    def execute(self, achar_todas=False, usar_vizinhanca_controlada=False):
        inicio = time.perf_counter()
        lim_inf = 0
        lim_sup = 7
        dim = 8
        solucoes = set()
        solucoes_f = []
        max_solucoes = 92 if achar_todas else 1
        total_interacoes = 0
        rodada = 0
        modo = (
            "Controlada (Unitária)"
            if usar_vizinhanca_controlada
            else "Ampla (Acesso Total)"
        )

        while len(solucoes) < max_solucoes:
            rodada += 1
            x_best = np.random.randint(lim_inf, lim_sup + 1, size=dim)
            f_best = self.func(x_best)
            temperatura = TEMPERATURA_INICIAL
            interacoes = 0

            while interacoes < 1000 and temperatura > 0.01:
                interacoes += 1
                total_interacoes += 1
                x_cand = x_best.copy()

                if usar_vizinhanca_controlada:
                    x_cand = self.get_vizinho_controlado(x_best)
                else:
                    col = np.random.randint(0, dim)
                    nova_linha = np.random.randint(lim_inf, lim_sup + 1)

                    while nova_linha == x_cand[col]:
                        nova_linha = np.random.randint(lim_inf, lim_sup + 1)

                    x_cand[col] = nova_linha

                f_cand = self.func(x_cand)
                delta_f = f_cand - f_best

                aceita = False

                if delta_f >= 0:
                    aceita = True

                else:
                    p = np.exp(delta_f / temperatura)
                    if p >= np.random.rand():
                        aceita = True

                if aceita:
                    x_best = x_cand
                    f_best = f_cand

                temperatura *= FATOR_RESFRIAMENTO

                helper.print_com_flush(
                    f"Rodada: {rodada} - Iter: {total_interacoes} - Achados: {len(solucoes)}"
                )

                if f_best == 28:
                    solucoes.add(tuple(x_best.tolist()))
                    solucoes_f.append(28)
                    break

        fim = time.perf_counter()
        tempo_total = fim - inicio

        print("\n--- RESULTADOS FINAIS ---")
        print(f"Total de Soluções Encontradas: {len(solucoes)}")
        print(f"Total de Interações (Passos): {total_interacoes}")
        print(f"Duração Total: {tempo_total:.2f} segundos")
        for i, solucao in enumerate(solucoes):
            solucao_str = str(solucao)
            print(f"[{i + 1:02d}] {solucao_str}")
        print("\n")
        print(f"Modo de Perturbação Utilizado: {modo}")
        print(f"Temperadura Inicial: {TEMPERATURA_INICIAL}")
        print(f"Fator de Resfriamento: {FATOR_RESFRIAMENTO}")
        print("Decaimento: temperatura * fator de resfriamento (0,99)")

        return (solucoes, solucoes_f)

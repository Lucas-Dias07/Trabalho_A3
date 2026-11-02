
import sys
import random
from collections import deque

import pygame

# ==========================================
# CONFIGURACOES
# ==========================================

pygame.init()

CELULA = 40
COLUNAS = 19
LINHAS = 13

LARGURA = COLUNAS * CELULA
ALTURA_MAPA = LINHAS * CELULA
ALTURA = ALTURA_MAPA + 100

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto dos Enigmas")

RELOGIO = pygame.time.Clock()

FONTE = pygame.font.SysFont("Arial", 19)
FONTE_GRANDE = pygame.font.SysFont("Arial", 30, bold=True)

# Paleta de cores
CORES = {
    "fundo": (23, 28, 38),
    "parede": (55, 67, 85),
    "chao": (239, 236, 224),
    "jogador": (55, 130, 220),
    "chave": (245, 190, 45),
    "enigma": (160, 95, 210),
    "porta": (175, 75, 65),
    "saida": (65, 165, 105),
    "branco": (250, 250, 250),
    "dica": (255, 190, 55)
}


# ==========================================
# ENIGMAS
# ==========================================

ENIGMAS = [
    {
        "pergunta": "Complete: 2, 4, 8, 16, ?",
        "resposta": "32",
        "dica": "Observe a operacao realizada entre um numero e o seguinte.",
        "explicacao": "Cada numero e o dobro do anterior."
    },
    {
        "pergunta": "Complete: 1, 1, 2, 3, 5, ?",
        "resposta": "8",
        "dica": "Observe a relacao entre os dois numeros anteriores.",
        "explicacao": "Cada numero e a soma dos dois anteriores."
    },
    {
        "pergunta": "Complete: 1, 4, 9, 16, ?",
        "resposta": "25",
        "dica": "Esses numeros sao resultados de um numero multiplicado por ele mesmo.",
        "explicacao": "Sao os quadrados de 1, 2, 3, 4 e 5."
    }
]


# ==========================================
# QUEBRA AUTOMATICA DE TEXTO
# ==========================================

def quebrar_texto(texto, fonte, largura_maxima):

    palavras = texto.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:

        teste = linha_atual + " " + palavra

        if fonte.size(teste.strip())[0] <= largura_maxima:
            linha_atual = teste.strip()

        else:
            if linha_atual:
                linhas.append(linha_atual)

            linha_atual = palavra

    if linha_atual:
        linhas.append(linha_atual)

    return linhas


def desenhar_texto(texto, x, y, cor=None, fonte=None):

    if cor is None:
        cor = CORES["branco"]

    if fonte is None:
        fonte = FONTE

    imagem = fonte.render(texto, True, cor)
    TELA.blit(imagem, (x, y))


def desenhar_texto_quebrado(texto, x, y, largura, cor=None):

    if cor is None:
        cor = CORES["branco"]

    linhas = quebrar_texto(texto, FONTE, largura)

    for i, linha in enumerate(linhas):

        desenhar_texto(
            linha,
            x,
            y + i * 25,
            cor
        )


# ==========================================
# GERACAO ALEATORIA DO LABIRINTO
# ==========================================

def gerar_labirinto():

    mapa = [
        ["#" for _ in range(COLUNAS)]
        for _ in range(LINHAS)
    ]

    inicio = (1, 1)
    mapa[1][1] = "."

    pilha = [inicio]

    direcoes = [
        (-2, 0),
        (2, 0),
        (0, -2),
        (0, 2)
    ]

    # Busca em profundidade para gerar caminhos
    while pilha:

        linha, coluna = pilha[-1]

        opcoes = direcoes[:]
        random.shuffle(opcoes)

        encontrou = False

        for dl, dc in opcoes:

            nova_linha = linha + dl
            nova_coluna = coluna + dc

            if not (
                1 <= nova_linha < LINHAS - 1
                and 1 <= nova_coluna < COLUNAS - 1
            ):
                continue

            if mapa[nova_linha][nova_coluna] != "#":
                continue

            mapa[linha + dl // 2][coluna + dc // 2] = "."
            mapa[nova_linha][nova_coluna] = "."

            pilha.append((nova_linha, nova_coluna))

            encontrou = True
            break

        if not encontrou:
            pilha.pop()

    saida = (LINHAS - 2, COLUNAS - 2)

    mapa[saida[0]][saida[1]] = "S"

    return mapa, inicio, saida


# ==========================================
# GRAFO E BUSCA EM LARGURA
# ==========================================

def obter_vizinhos(mapa, posicao, porta_aberta):

    linha, coluna = posicao

    movimentos = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    resultado = []

    for dl, dc in movimentos:

        nl = linha + dl
        nc = coluna + dc

        if not (0 <= nl < LINHAS and 0 <= nc < COLUNAS):
            continue

        celula = mapa[nl][nc]

        if celula == "#":
            continue

        if celula == "D" and not porta_aberta:
            continue

        resultado.append((nl, nc))

    return resultado


def busca_em_largura(mapa, inicio, destino, porta_aberta):

    fila = deque([[inicio]])
    visitados = {inicio}

    while fila:

        caminho = fila.popleft()
        atual = caminho[-1]

        if atual == destino:
            return caminho

        for vizinho in obter_vizinhos(
            mapa, atual, porta_aberta
        ):

            if vizinho not in visitados:

                visitados.add(vizinho)
                fila.append(caminho + [vizinho])

    return []


# ==========================================
# CRIACAO DE UMA FASE
# ==========================================

def iniciar_fase(numero):

    mapa, inicio, saida = gerar_labirinto()

    caminho_principal = busca_em_largura(
        mapa, inicio, saida, True
    )

    # Posiciona a porta no caminho da saida
    indice_porta = max(
        2,
        min(
            int(len(caminho_principal) * 0.65),
            len(caminho_principal) - 2
        )
    )

    porta = caminho_principal[indice_porta]

    mapa[porta[0]][porta[1]] = "D"

    # Descobre todas as posicoes acessiveis antes da porta
    fila = deque([inicio])
    visitados = {inicio}

    while fila:

        atual = fila.popleft()

        for vizinho in obter_vizinhos(
            mapa, atual, False
        ):

            if vizinho not in visitados:

                visitados.add(vizinho)
                fila.append(vizinho)

    candidatos = [
        pos for pos in visitados
        if pos != inicio and pos != porta
    ]

    # Sorteia chave e enigma
    chave, enigma = random.sample(candidatos, 2)

    mapa[chave[0]][chave[1]] = "K"
    mapa[enigma[0]][enigma[1]] = "E"

    return {
        "mapa": mapa,
        "jogador": inicio,
        "chave": chave,
        "enigma": enigma,
        "porta": porta,
        "saida": saida,
        "tem_chave": False,
        "enigma_resolvido": False,
        "numero": numero
    }


# ==========================================
# OBJETIVO ATUAL
# ==========================================

def obter_objetivo(fase):

    if not fase["tem_chave"]:
        return fase["chave"]

    if not fase["enigma_resolvido"]:
        return fase["enigma"]

    return fase["saida"]


# ==========================================
# DESENHO DO MAPA
# ==========================================

def desenhar_mapa(fase, caminho_dica):

    TELA.fill(CORES["fundo"])

    mapa = fase["mapa"]

    for linha in range(LINHAS):

        for coluna in range(COLUNAS):

            x = coluna * CELULA
            y = linha * CELULA

            celula = mapa[linha][coluna]

            if celula == "#":
                cor = CORES["parede"]
            else:
                cor = CORES["chao"]

            pygame.draw.rect(
                TELA,
                cor,
                (x, y, CELULA, CELULA)
            )

            pygame.draw.rect(
                TELA,
                (210, 207, 196),
                (x, y, CELULA, CELULA),
                1
            )

            centro = (
                x + CELULA // 2,
                y + CELULA // 2
            )

            if celula == "K":

                pygame.draw.circle(
                    TELA,
                    CORES["chave"],
                    centro,
                    11
                )

            elif celula == "D":

                pygame.draw.rect(
                    TELA,
                    CORES["porta"],
                    (x + 9, y + 5, 22, 30)
                )

            elif celula == "E":

                pygame.draw.circle(
                    TELA,
                    CORES["enigma"],
                    centro,
                    13
                )

                desenhar_texto(
                    "?",
                    x + 14,
                    y + 8,
                    CORES["branco"]
                )

            elif celula == "S":

                pygame.draw.circle(
                    TELA,
                    CORES["saida"],
                    centro,
                    13
                )

    # Caminho sugerido pela BFS
    for linha, coluna in caminho_dica[1:]:

        x = coluna * CELULA + CELULA // 2
        y = linha * CELULA + CELULA // 2

        pygame.draw.circle(
            TELA,
            CORES["dica"],
            (x, y),
            5
        )

    # Jogador
    linha, coluna = fase["jogador"]

    x = coluna * CELULA + CELULA // 2
    y = linha * CELULA + CELULA // 2

    pygame.draw.circle(
        TELA,
        CORES["jogador"],
        (x, y),
        13
    )


# ==========================================
# TELA DE INFORMACOES
# ==========================================

def desenhar_hud(fase, pontuacao, mensagem):

    pygame.draw.rect(
        TELA,
        CORES["fundo"],
        (0, ALTURA_MAPA, LARGURA, 100)
    )

    desenhar_texto_quebrado(
        mensagem,
        12,
        525,
        LARGURA - 24,
        CORES["dica"]
    )

    desenhar_texto(
        f"Fase: {fase['numero']}/3",
        12,
        552
    )

    desenhar_texto(
        f"Pontos: {pontuacao}",
        180,
        552,
        CORES["chave"]
    )

    status_chave = "SIM" if fase["tem_chave"] else "NAO"
    status_enigma = "SIM" if fase["enigma_resolvido"] else "NAO"

    desenhar_texto(
        f"Chave: {status_chave} | Enigma: {status_enigma}",
        350,
        552
    )

    desenhar_texto(
        "Setas/WASD: mover | H: caminho | I: dica | R: reiniciar",
        12,
        585
    )


# ==========================================
# JANELA DO ENIGMA
# ==========================================

def desenhar_enigma(numero, resposta, mostrar_dica):

    enigma = ENIGMAS[numero]

    pygame.draw.rect(
        TELA,
        CORES["fundo"],
        (65, 145, 630, 245)
    )

    pygame.draw.rect(
        TELA,
        CORES["enigma"],
        (65, 145, 630, 245),
        3
    )

    desenhar_texto(
        "RESOLVA O DESAFIO",
        220,
        165,
        CORES["chave"],
        FONTE_GRANDE
    )

    desenhar_texto(
        enigma["pergunta"],
        105,
        220
    )

    desenhar_texto(
        "Resposta: " + resposta + "_",
        105,
        260,
        CORES["chave"]
    )

    if mostrar_dica:

        # Quebra a dica em linhas automaticamente
        desenhar_texto_quebrado(
            "DICA: " + enigma["dica"],
            105,
            300,
            540,
            CORES["dica"]
        )

    else:

        desenhar_texto(
            "Pressione I para receber uma dica.",
            105,
            305,
            CORES["dica"]
        )

    desenhar_texto(
        "ENTER: confirmar resposta",
        105,
        350
    )


# ==========================================
# JOGO PRINCIPAL
# ==========================================

def main():

    fase_atual = 0
    pontuacao = 0

    fase = iniciar_fase(1)

    estado = "jogando"

    resposta = ""
    mostrar_dica = False
    caminho_dica = []

    mensagem = "Encontre a chave!"

    rodando = True

    while rodando:

        RELOGIO.tick(60)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type != pygame.KEYDOWN:
                continue

            if evento.key == pygame.K_ESCAPE:
                rodando = False
                continue

            # Vitoria final
            if estado == "vitoria":

                if evento.key == pygame.K_r:

                    fase_atual = 0
                    pontuacao = 0

                    fase = iniciar_fase(1)

                    estado = "jogando"
                    mensagem = "Encontre a chave!"

                continue

            # Fase concluida
            if estado == "fase_concluida":

                if evento.key == pygame.K_RETURN:

                    fase_atual += 1

                    if fase_atual >= len(ENIGMAS):

                        estado = "vitoria"

                    else:

                        fase = iniciar_fase(fase_atual + 1)

                        estado = "jogando"
                        mensagem = "Novo labirinto! Encontre a chave!"

                        caminho_dica = []

                continue

            # Resolvendo enigma
            if estado == "respondendo":

                if evento.key == pygame.K_i:

                    mostrar_dica = True

                elif evento.key == pygame.K_RETURN:

                    enigma = ENIGMAS[fase_atual]

                    if resposta.strip() == enigma["resposta"]:

                        fase["enigma_resolvido"] = True

                        el, ec = fase["enigma"]
                        fase["mapa"][el][ec] = "."

                        pl, pc = fase["porta"]
                        fase["mapa"][pl][pc] = "."

                        pontuacao += 100

                        mensagem = enigma["explicacao"]

                        estado = "jogando"
                        mostrar_dica = False
                        resposta = ""

                    else:

                        mensagem = "Resposta incorreta. Tente novamente!"
                        resposta = ""

                elif evento.key == pygame.K_BACKSPACE:

                    resposta = resposta[:-1]

                elif evento.unicode.isdigit():

                    resposta += evento.unicode

                continue

            # Dica de caminho
            if evento.key == pygame.K_h:

                objetivo = obter_objetivo(fase)

                if objetivo is not None:

                    caminho_dica = busca_em_largura(
                        fase["mapa"],
                        fase["jogador"],
                        objetivo,
                        fase["enigma_resolvido"]
                    )

                continue

            # Reiniciar jogo
            if evento.key == pygame.K_r:

                fase_atual = 0
                pontuacao = 0

                fase = iniciar_fase(1)

                caminho_dica = []
                resposta = ""
                mostrar_dica = False

                estado = "jogando"
                mensagem = "Jogo reiniciado!"

                continue

            # Movimentacao
            movimentos = {
                pygame.K_UP: (-1, 0),
                pygame.K_DOWN: (1, 0),
                pygame.K_LEFT: (0, -1),
                pygame.K_RIGHT: (0, 1),
                pygame.K_w: (-1, 0),
                pygame.K_s: (1, 0),
                pygame.K_a: (0, -1),
                pygame.K_d: (0, 1)
            }

            if evento.key not in movimentos:
                continue

            dl, dc = movimentos[evento.key]

            linha, coluna = fase["jogador"]

            nova_posicao = (
                linha + dl,
                coluna + dc
            )

            if nova_posicao not in obter_vizinhos(
                fase["mapa"],
                fase["jogador"],
                fase["enigma_resolvido"]
            ):
                continue

            # Saida
            if nova_posicao == fase["saida"]:

                if (
                    fase["tem_chave"]
                    and fase["enigma_resolvido"]
                ):

                    pontuacao += 150
                    estado = "fase_concluida"

                else:

                    mensagem = "Voce precisa da chave e do enigma resolvido!"

                continue

            fase["jogador"] = nova_posicao

            caminho_dica = []

            # Coletar chave
            if nova_posicao == fase["chave"]:

                fase["tem_chave"] = True

                kl, kc = fase["chave"]
                fase["mapa"][kl][kc] = "."

                fase["chave"] = None

                pontuacao += 50

                mensagem = "Chave encontrada! Procure o enigma."

            # Encontrar enigma
            elif nova_posicao == fase["enigma"]:

                estado = "respondendo"

                resposta = ""
                mostrar_dica = False

                mensagem = "Resolva o desafio!"

        # Desenho
        desenhar_mapa(fase, caminho_dica)

        desenhar_hud(
            fase,
            pontuacao,
            mensagem
        )

        if estado == "respondendo":

            desenhar_enigma(
                fase_atual,
                resposta,
                mostrar_dica
            )

        elif estado == "fase_concluida":

            pygame.draw.rect(
                TELA,
                CORES["fundo"],
                (100, 180, 560, 180)
            )

            desenhar_texto(
                "FASE CONCLUIDA!",
                235,
                215,
                CORES["saida"],
                FONTE_GRANDE
            )

            desenhar_texto(
                "Voce encontrou a saida!",
                220,
                270
            )

            desenhar_texto(
                "Pressione ENTER para continuar",
                165,
                320,
                CORES["chave"]
            )

        elif estado == "vitoria":

            pygame.draw.rect(
                TELA,
                CORES["fundo"],
                (70, 160, 620, 230)
            )

            desenhar_texto(
                "PARABENS!",
                280,
                195,
                CORES["saida"],
                FONTE_GRANDE
            )

            desenhar_texto(
                "Voce concluiu os tres desafios!",
                170,
                255
            )

            desenhar_texto(
                f"Pontuacao final: {pontuacao}",
                230,
                300,
                CORES["chave"]
            )

            desenhar_texto(
                "Pressione R para jogar novamente",
                175,
                350
            )

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()


import sys
import random
import math
from collections import deque

import pygame


# =========================================================
# CONFIGURACOES
# =========================================================

pygame.init()

CELULA = 40
COLUNAS = 25
LINHAS = 17

LARGURA = COLUNAS * CELULA
ALTURA_MAPA = LINHAS * CELULA
ALTURA_HUD = 110
ALTURA = ALTURA_MAPA + ALTURA_HUD

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto dos Enigmas - Masmorra Fantastica")

RELOGIO = pygame.time.Clock()

FONTE = pygame.font.SysFont("Arial", 17)
FONTE_PEQUENA = pygame.font.SysFont("Arial", 13)
FONTE_GRANDE = pygame.font.SysFont("Arial", 27, bold=True)
FONTE_TITULO = pygame.font.SysFont("Georgia", 23, bold=True)


CORES = {
    "fundo": (20, 19, 30),
    "painel": (39, 34, 49),
    "painel_borda": (126, 91, 57),

    "pedra": (75, 72, 83),
    "pedra_clara": (105, 99, 109),
    "pedra_escura": (45, 43, 54),

    "chao": (82, 73, 76),
    "chao_claro": (105, 91, 88),
    "chao_escuro": (61, 55, 63),

    "dourado": (236, 184, 76),
    "dourado_claro": (255, 219, 125),

    "roxo": (132, 86, 183),
    "roxo_claro": (190, 140, 230),

    "verde": (88, 174, 125),
    "branco": (245, 239, 228),
    "texto_secundario": (190, 177, 171),
    "dica": (255, 205, 93)
}


# =========================================================
# ENIGMAS
# =========================================================

ENIGMAS = [
    {
        "pergunta": "Complete: 2, 4, 8, 16, ?",
        "resposta": "32",
        "dica": "Observe a operacao entre um numero e o seguinte.",
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
        "dica": "Os numeros sao resultados de um numero multiplicado por ele mesmo.",
        "explicacao": "Sao os quadrados de 1, 2, 3, 4 e 5."
    }
]


# =========================================================
# TEXTO
# =========================================================

def desenhar_texto(texto, x, y, cor=None, fonte=None):
    if cor is None:
        cor = CORES["branco"]

    if fonte is None:
        fonte = FONTE

    imagem = fonte.render(str(texto), True, cor)
    TELA.blit(imagem, (x, y))


def desenhar_texto_centralizado(texto, x, y, cor=None, fonte=None):
    if cor is None:
        cor = CORES["branco"]

    if fonte is None:
        fonte = FONTE

    imagem = fonte.render(str(texto), True, cor)
    retangulo = imagem.get_rect(center=(x, y))
    TELA.blit(imagem, retangulo)


def quebrar_texto(texto, fonte, largura):
    palavras = texto.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        teste = (linha_atual + " " + palavra).strip()

        if fonte.size(teste)[0] <= largura:
            linha_atual = teste
        else:
            if linha_atual:
                linhas.append(linha_atual)

            linha_atual = palavra

    if linha_atual:
        linhas.append(linha_atual)

    return linhas


# =========================================================
# DESENHO DO CENARIO
# =========================================================

def desenhar_chao(x, y):
    pygame.draw.rect(
        TELA,
        CORES["chao"],
        (x, y, CELULA, CELULA)
    )

    pygame.draw.rect(
        TELA,
        CORES["chao_claro"],
        (x + 2, y + 2, CELULA - 4, CELULA - 4),
        1
    )

    pygame.draw.line(
        TELA,
        CORES["chao_escuro"],
        (x + 5, y + 33),
        (x + 17, y + 33),
        2
    )


def desenhar_parede(x, y):
    pygame.draw.rect(
        TELA,
        CORES["pedra"],
        (x, y, CELULA, CELULA)
    )

    pygame.draw.rect(
        TELA,
        CORES["pedra_clara"],
        (x + 2, y + 2, CELULA - 4, 5)
    )

    pygame.draw.rect(
        TELA,
        CORES["pedra_escura"],
        (x + 2, y + 33, CELULA - 4, 5)
    )

    pygame.draw.line(
        TELA,
        CORES["pedra_escura"],
        (x + 20, y + 2),
        (x + 20, y + 16),
        2
    )

    pygame.draw.line(
        TELA,
        CORES["pedra_escura"],
        (x + 8, y + 20),
        (x + 30, y + 20),
        2
    )


# =========================================================
# PERSONAGEM
# =========================================================

def desenhar_jogador(posicao):
    linha, coluna = posicao

    x = coluna * CELULA + CELULA // 2
    y = linha * CELULA + CELULA // 2

    pygame.draw.ellipse(
        TELA,
        (35, 30, 35),
        (x - 12, y + 7, 25, 9)
    )

    pygame.draw.circle(
        TELA,
        (74, 116, 171),
        (x, y + 2),
        11
    )

    pygame.draw.circle(
        TELA,
        (231, 193, 148),
        (x, y - 3),
        8
    )

    pygame.draw.arc(
        TELA,
        CORES["dourado"],
        (x - 9, y - 13, 18, 17),
        math.pi,
        math.tau,
        4
    )

    pygame.draw.line(
        TELA,
        CORES["dourado"],
        (x - 10, y - 5),
        (x + 10, y - 5),
        3
    )

    pygame.draw.circle(
        TELA,
        (35, 30, 30),
        (x + 3, y - 3),
        2
    )


# =========================================================
# ITENS
# =========================================================

def desenhar_chave(x, y):
    centro = (x + CELULA // 2, y + CELULA // 2)

    pygame.draw.circle(
        TELA,
        CORES["dourado"],
        centro,
        9,
        4
    )

    pygame.draw.line(
        TELA,
        CORES["dourado"],
        (centro[0] + 8, centro[1]),
        (centro[0] + 16, centro[1]),
        4
    )

    pygame.draw.line(
        TELA,
        CORES["dourado"],
        (centro[0] + 12, centro[1]),
        (centro[0] + 12, centro[1] + 5),
        3
    )


def desenhar_cristal(x, y, tempo):
    centro_x = x + CELULA // 2
    centro_y = y + CELULA // 2

    brilho = math.sin(tempo * 0.006) * 3

    pontos = [
        (centro_x, centro_y - 13 - brilho),
        (centro_x + 10, centro_y),
        (centro_x, centro_y + 13 + brilho),
        (centro_x - 10, centro_y)
    ]

    pygame.draw.polygon(TELA, CORES["roxo"], pontos)
    pygame.draw.polygon(TELA, CORES["roxo_claro"], pontos, 2)


def desenhar_porta(x, y):
    pygame.draw.rect(
        TELA,
        (91, 54, 48),
        (x + 5, y + 3, 30, 35)
    )

    pygame.draw.rect(
        TELA,
        CORES["dourado"],
        (x + 8, y + 6, 24, 29),
        2
    )

    pygame.draw.circle(
        TELA,
        CORES["dourado_claro"],
        (x + 27, y + 22),
        3
    )


def desenhar_saida(x, y, tempo):
    centro = (x + CELULA // 2, y + CELULA // 2)

    brilho = int(3 * math.sin(tempo * 0.006))

    pygame.draw.circle(
        TELA,
        (42, 105, 91),
        centro,
        16 + brilho
    )

    pygame.draw.circle(
        TELA,
        (102, 221, 173),
        centro,
        12,
        3
    )

    pygame.draw.circle(
        TELA,
        (190, 255, 218),
        centro,
        5
    )


# =========================================================
# GERACAO DO LABIRINTO - DFS
# =========================================================

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

    while pilha:
        linha, coluna = pilha[-1]

        opcoes = direcoes[:]
        random.shuffle(opcoes)

        encontrou = False

        for dl, dc in opcoes:
            nl = linha + dl
            nc = coluna + dc

            if not (
                1 <= nl < LINHAS - 1
                and 1 <= nc < COLUNAS - 1
            ):
                continue

            if mapa[nl][nc] != "#":
                continue

            mapa[linha + dl // 2][coluna + dc // 2] = "."
            mapa[nl][nc] = "."

            pilha.append((nl, nc))
            encontrou = True
            break

        if not encontrou:
            pilha.pop()

    saida = (LINHAS - 2, COLUNAS - 2)

    # Garante que exista um corredor ate o portal.
    mapa[saida[0]][saida[1]] = "."

    # A porta fica imediatamente antes do portal.
    porta = (saida[0], saida[1] - 1)

    # Garante a passagem entre a porta e o restante do labirinto.
    mapa[porta[0]][porta[1]] = "."

    mapa[saida[0]][saida[1]] = "S"
    mapa[porta[0]][porta[1]] = "D"

    return mapa, inicio, saida, porta


# =========================================================
# BUSCA EM LARGURA - BFS
# =========================================================

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
            mapa,
            atual,
            porta_aberta
        ):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(caminho + [vizinho])

    return []


# =========================================================
# POSICIONAMENTO ESPALHADO DOS ITENS
# =========================================================

def distancia(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def escolher_posicoes_espalhadas(candidatos, quantidade, distancia_minima):
    """
    Escolhe posicoes aleatorias tentando manter distancia
    entre as chaves e o cristal.
    """

    candidatos = candidatos[:]
    random.shuffle(candidatos)

    escolhidas = []

    for posicao in candidatos:
        if all(
            distancia(posicao, outra) >= distancia_minima
            for outra in escolhidas
        ):
            escolhidas.append(posicao)

            if len(escolhidas) == quantidade:
                return escolhidas

    # Se nao houver espaco suficiente, completa com posicoes
    # ainda nao utilizadas, sem repetir casas.
    for posicao in candidatos:
        if posicao not in escolhidas:
            escolhidas.append(posicao)

            if len(escolhidas) == quantidade:
                break

    return escolhidas


# =========================================================
# CRIACAO DA FASE
# =========================================================

def iniciar_fase(numero):
    mapa, inicio, saida, porta = gerar_labirinto()

    # Descobre todas as casas acessiveis antes da porta.
    fila = deque([inicio])
    visitados = {inicio}

    while fila:
        atual = fila.popleft()

        for vizinho in obter_vizinhos(
            mapa,
            atual,
            False
        ):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    # 2 chaves na fase 1, 3 na fase 2 e 4 na fase 3.
    total_chaves = numero + 1

    # Retira inicio e porta das possibilidades.
    candidatos = [
        posicao
        for posicao in visitados
        if posicao != inicio and posicao != porta
    ]

    # Seleciona as chaves e o cristal em locais diferentes.
    posicoes = escolher_posicoes_espalhadas(
        candidatos,
        total_chaves + 1,
        distancia_minima=5
    )

    chaves = posicoes[:total_chaves]
    enigma = posicoes[total_chaves]

    for linha, coluna in chaves:
        mapa[linha][coluna] = "K"

    mapa[enigma[0]][enigma[1]] = "E"

    return {
        "mapa": mapa,
        "jogador": inicio,
        "chaves": chaves,
        "total_chaves": total_chaves,
        "chaves_coletadas": 0,
        "enigma": enigma,
        "porta": porta,
        "saida": saida,
        "enigma_resolvido": False,
        "numero": numero
    }


# =========================================================
# OBJETIVOS
# =========================================================

def porta_esta_aberta(fase):
    return (
        fase["enigma_resolvido"]
        and fase["chaves_coletadas"] == fase["total_chaves"]
    )


def obter_objetivo(fase):
    if fase["chaves"]:
        return fase["chaves"][0]

    if not fase["enigma_resolvido"]:
        return fase["enigma"]

    return fase["saida"]


# =========================================================
# DESENHO DO MAPA
# =========================================================

def desenhar_mapa(fase, caminho_dica):
    TELA.fill(CORES["fundo"])

    mapa = fase["mapa"]
    tempo = pygame.time.get_ticks()

    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            x = coluna * CELULA
            y = linha * CELULA

            celula = mapa[linha][coluna]

            if celula == "#":
                desenhar_parede(x, y)
            else:
                desenhar_chao(x, y)

            if celula == "K":
                desenhar_chave(x, y)

            elif celula == "D":
                desenhar_porta(x, y)

            elif celula == "E":
                desenhar_cristal(x, y, tempo)

            elif celula == "S":
                desenhar_saida(x, y, tempo)

    # Caminho sugerido pela BFS.
    for linha, coluna in caminho_dica[1:]:
        x = coluna * CELULA + CELULA // 2
        y = linha * CELULA + CELULA // 2

        pygame.draw.circle(
            TELA,
            CORES["dica"],
            (x, y),
            5
        )

    desenhar_jogador(fase["jogador"])


# =========================================================
# HUD
# =========================================================

def desenhar_hud(fase, mensagem):
    y = ALTURA_MAPA

    pygame.draw.rect(
        TELA,
        CORES["painel"],
        (0, y, LARGURA, ALTURA_HUD)
    )

    pygame.draw.line(
        TELA,
        CORES["painel_borda"],
        (0, y),
        (LARGURA, y),
        3
    )

    desenhar_texto(
        f"MASMORRA  |  FASE {fase['numero']}/3",
        15,
        y + 12,
        CORES["dourado"],
        FONTE_GRANDE
    )

    quantidade = fase["chaves_coletadas"]
    total = fase["total_chaves"]

    cor_chaves = (
        CORES["verde"]
        if quantidade == total
        else CORES["texto_secundario"]
    )

    desenhar_texto(
        f"Chaves encontradas: {quantidade}/{total}",
        15,
        y + 55,
        cor_chaves,
        FONTE_PEQUENA
    )

    status_enigma = (
        "Resolvido"
        if fase["enigma_resolvido"]
        else "Pendente"
    )

    desenhar_texto(
        f"Enigma: {status_enigma}",
        260,
        y + 55,
        CORES["texto_secundario"],
        FONTE_PEQUENA
    )

    desenhar_texto(
        mensagem,
        15,
        y + 82,
        CORES["dourado_claro"],
        FONTE_PEQUENA
    )


# =========================================================
# JANELA DO ENIGMA
# =========================================================

def desenhar_enigma(numero, resposta, mostrar_dica):
    enigma = ENIGMAS[numero]

    sobreposicao = pygame.Surface((LARGURA, ALTURA))
    sobreposicao.set_alpha(150)
    sobreposicao.fill((0, 0, 0))
    TELA.blit(sobreposicao, (0, 0))

    painel = pygame.Rect(
        55,
        135,
        LARGURA - 110,
        280
    )

    pygame.draw.rect(
        TELA,
        (48, 37, 49),
        painel,
        border_radius=14
    )

    pygame.draw.rect(
        TELA,
        CORES["dourado"],
        painel,
        3,
        border_radius=14
    )

    desenhar_texto_centralizado(
        "O CRISTAL DOS ENIGMAS",
        LARGURA // 2,
        175,
        CORES["dourado_claro"],
        FONTE_TITULO
    )

    desenhar_texto_centralizado(
        enigma["pergunta"],
        LARGURA // 2,
        225,
        CORES["branco"],
        FONTE_GRANDE
    )

    pygame.draw.rect(
        TELA,
        (30, 27, 37),
        (145, 260, 470, 43),
        border_radius=7
    )

    pygame.draw.rect(
        TELA,
        CORES["painel_borda"],
        (145, 260, 470, 43),
        2,
        border_radius=7
    )

    desenhar_texto(
        "RESPOSTA: " + resposta + "_",
        165,
        269,
        CORES["dourado_claro"],
        FONTE
    )

    if mostrar_dica:
        linhas = quebrar_texto(
            "DICA: " + enigma["dica"],
            FONTE_PEQUENA,
            470
        )

        for i, linha in enumerate(linhas):
            desenhar_texto(
                linha,
                145,
                315 + i * 19,
                CORES["dica"],
                FONTE_PEQUENA
            )
    else:
        desenhar_texto_centralizado(
            "Pressione I para revelar uma dica",
            LARGURA // 2,
            335,
            CORES["texto_secundario"],
            FONTE_PEQUENA
        )

    desenhar_texto_centralizado(
        "ENTER: confirmar resposta",
        LARGURA // 2,
        385,
        CORES["dourado"],
        FONTE_PEQUENA
    )


# =========================================================
# TELAS DE CONCLUSAO
# =========================================================

def desenhar_tela_conclusao(titulo, descricao, instrucao):
    sobreposicao = pygame.Surface((LARGURA, ALTURA))
    sobreposicao.set_alpha(190)
    sobreposicao.fill((0, 0, 0))
    TELA.blit(sobreposicao, (0, 0))

    painel = pygame.Rect(
        70,
        165,
        LARGURA - 140,
        220
    )

    pygame.draw.rect(
        TELA,
        CORES["painel"],
        painel,
        border_radius=15
    )

    pygame.draw.rect(
        TELA,
        CORES["dourado"],
        painel,
        3,
        border_radius=15
    )

    desenhar_texto_centralizado(
        titulo,
        LARGURA // 2,
        215,
        CORES["dourado"],
        FONTE_GRANDE
    )

    desenhar_texto_centralizado(
        descricao,
        LARGURA // 2,
        270,
        CORES["branco"],
        FONTE
    )

    desenhar_texto_centralizado(
        instrucao,
        LARGURA // 2,
        330,
        CORES["dourado_claro"],
        FONTE
    )


# =========================================================
# JOGO PRINCIPAL
# =========================================================

def main():
    fase_atual = 0
    fase = iniciar_fase(1)

    estado = "jogando"

    resposta = ""
    mostrar_dica = False
    caminho_dica = []

    mensagem = "Explore a masmorra e encontre todas as chaves!"

    rodando = True

    while rodando:
        RELOGIO.tick(60)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False
                continue

            if evento.type != pygame.KEYDOWN:
                continue

            if evento.key == pygame.K_ESCAPE:
                rodando = False
                continue

            # -------------------------------------------------
            # VITORIA
            # -------------------------------------------------

            if estado == "vitoria":
                if evento.key == pygame.K_r:
                    fase_atual = 0
                    fase = iniciar_fase(1)

                    estado = "jogando"
                    mensagem = "Explore a masmorra e encontre todas as chaves!"
                    caminho_dica = []

                continue

            # -------------------------------------------------
            # FASE CONCLUIDA
            # -------------------------------------------------

            if estado == "fase_concluida":
                if evento.key == pygame.K_RETURN:
                    fase_atual += 1

                    if fase_atual >= len(ENIGMAS):
                        estado = "vitoria"
                    else:
                        fase = iniciar_fase(fase_atual + 1)

                        estado = "jogando"
                        mensagem = "Nova fase! Explore a masmorra!"
                        caminho_dica = []

                continue

            # -------------------------------------------------
            # RESPONDENDO AO ENIGMA
            # -------------------------------------------------

            if estado == "respondendo":

                if evento.key == pygame.K_i:
                    mostrar_dica = True

                elif evento.key == pygame.K_RETURN:
                    enigma = ENIGMAS[fase_atual]

                    if resposta.strip() == enigma["resposta"]:
                        fase["enigma_resolvido"] = True

                        # O cristal desaparece definitivamente.
                        el, ec = fase["enigma"]
                        fase["mapa"][el][ec] = "."

                        mensagem = enigma["explicacao"]

                        # A porta so abre se todas as chaves
                        # ja tiverem sido encontradas.
                        if porta_esta_aberta(fase):
                            pl, pc = fase["porta"]
                            fase["mapa"][pl][pc] = "."

                            mensagem = "O enigma foi resolvido e a porta esta aberta!"

                        else:
                            mensagem = "Enigma resolvido! Ainda faltam chaves."

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

            # -------------------------------------------------
            # DICA DE CAMINHO
            # -------------------------------------------------

            if evento.key == pygame.K_h:
                objetivo = obter_objetivo(fase)

                caminho_dica = busca_em_largura(
                    fase["mapa"],
                    fase["jogador"],
                    objetivo,
                    porta_esta_aberta(fase)
                )

                continue

            # -------------------------------------------------
            # REINICIAR
            # -------------------------------------------------

            if evento.key == pygame.K_r:
                fase_atual = 0
                fase = iniciar_fase(1)

                caminho_dica = []
                resposta = ""
                mostrar_dica = False

                estado = "jogando"
                mensagem = "Masmorra reiniciada!"

                continue

            # -------------------------------------------------
            # MOVIMENTACAO
            # -------------------------------------------------

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

            vizinhos = obter_vizinhos(
                fase["mapa"],
                fase["jogador"],
                porta_esta_aberta(fase)
            )

            if nova_posicao not in vizinhos:
                continue

            # -------------------------------------------------
            # PORTAL
            # -------------------------------------------------

            if nova_posicao == fase["saida"]:

                if porta_esta_aberta(fase):
                    estado = "fase_concluida"
                    mensagem = "Voce conseguiu escapar da masmorra!"
                else:
                    mensagem = (
                        "Encontre todas as chaves e resolva o enigma "
                        "para abrir a porta!"
                    )

                continue

            fase["jogador"] = nova_posicao
            caminho_dica = []

            # -------------------------------------------------
            # COLETAR CHAVE
            # -------------------------------------------------

            if nova_posicao in fase["chaves"]:

                fase["chaves"].remove(nova_posicao)
                fase["chaves_coletadas"] += 1

                kl, kc = nova_posicao
                fase["mapa"][kl][kc] = "."

                quantidade = fase["chaves_coletadas"]
                total = fase["total_chaves"]

                mensagem = f"Chave encontrada! {quantidade}/{total}"

                # Verifica se esta era a ultima chave.
                if porta_esta_aberta(fase):
                    pl, pc = fase["porta"]
                    fase["mapa"][pl][pc] = "."

                    mensagem = "Todas as chaves encontradas! A porta abriu!"

            # -------------------------------------------------
            # ENCONTRAR O ENIGMA
            # -------------------------------------------------

            elif (
                nova_posicao == fase["enigma"]
                and not fase["enigma_resolvido"]
            ):
                estado = "respondendo"

                resposta = ""
                mostrar_dica = False

                mensagem = "Resolva o desafio matematico!"

        # =====================================================
        # DESENHO
        # =====================================================

        desenhar_mapa(fase, caminho_dica)
        desenhar_hud(fase, mensagem)

        if estado == "respondendo":
            desenhar_enigma(
                fase_atual,
                resposta,
                mostrar_dica
            )

        elif estado == "fase_concluida":
            desenhar_tela_conclusao(
                "FASE CONCLUIDA!",
                "Voce encontrou a saida da masmorra!",
                "Pressione ENTER para continuar"
            )

        elif estado == "vitoria":
            desenhar_tela_conclusao(
                "PARABENS, AVENTUREIRO!",
                "Voce concluiu os tres desafios!",
                "Pressione R para jogar novamente"
            )

        pygame.display.flip()

    pygame.quit()
    sys.exit()


# =========================================================
# EXECUCAO
# =========================================================

if __name__ == "__main__":
    main()

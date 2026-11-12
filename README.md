# 🗝️ Labirinto dos Enigmas

Um jogo de exploração e raciocínio lógico desenvolvido em **Python**, utilizando a biblioteca **Pygame**. O jogador precisa explorar labirintos, encontrar chaves espalhadas pelo mapa e resolver enigmas matemáticos para conseguir avançar pelas fases e encontrar a saída.

## 🎮 Sobre o projeto

O Labirinto dos Enigmas combina exploração, resolução de problemas e raciocínio lógico em uma experiência de jogo com temática de masmorra fantástica.

Cada fase apresenta um labirinto gerado aleatoriamente, aumentando o desafio conforme o jogador avança. Para completar cada etapa, é necessário explorar o ambiente, coletar todas as chaves exigidas, encontrar e resolver o enigma e, finalmente, liberar a passagem para a próxima fase.

## ✨ Funcionalidades

- **Labirintos aleatórios:** mapas gerados proceduralmente, proporcionando diferentes experiências a cada partida.
- **Progressão de dificuldade:** três fases com desafios progressivos.
- **Coleta de chaves:** quantidade crescente de chaves necessárias para avançar.
- **Enigmas matemáticos:** desafios envolvendo sequências numéricas e raciocínio lógico.
- **Sistema de portas:** a passagem só é liberada após cumprir os requisitos da fase.
- **Sistema de dicas:** possibilidade de solicitar ajuda para encontrar caminhos.
- **Ambientação temática:** visual inspirado em masmorras e aventuras fantásticas.

## 🧩 Enigmas do jogo

O jogo apresenta três desafios matemáticos:

| Fase | Desafio | Resposta |
|---|---|---|
| 1 | Sequência: 2, 4, 8, 16... | 32 |
| 2 | Sequência de Fibonacci | 8 |
| 3 | Sequência de números quadrados | 25 |

## 🕹️ Controles

| Tecla | Ação |
|---|---|
| W / ↑ | Movimentar para cima |
| S / ↓ | Movimentar para baixo |
| A / ← | Movimentar para esquerda |
| D / → | Movimentar para direita |
| H | Solicitar dica de caminho |
| I | Solicitar dica do enigma |
| Enter | Confirmar resposta |
| R | Reiniciar a fase |
| Esc | Sair do jogo |

## 🛠️ Tecnologias utilizadas

- **Python 3:** linguagem utilizada no desenvolvimento.
- **Pygame:** biblioteca responsável pelos elementos gráficos, movimentação, eventos e mecânicas do jogo.

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd NOME_DA_PASTA
```

### 3. Instale a dependência

```bash
pip install pygame
```

### 4. Execute o jogo

```bash
python jogo.py
```

## 🧠 Conceitos de Matemática Computacional aplicados

O desenvolvimento do jogo envolve conceitos importantes da Matemática Computacional e da Ciência da Computação:

- **Matrizes:** representação e organização dos mapas do labirinto.
- **Grafos:** modelagem das posições e caminhos possíveis dentro do labirinto.
- **Busca em largura (BFS):** algoritmo utilizado para encontrar caminhos e fornecer dicas ao jogador.
- **Busca em profundidade (DFS):** utilizada na geração procedural dos labirintos.
- **Lógica matemática:** aplicação de sequências numéricas e padrões na elaboração dos enigmas.
- **Algoritmos:** implementação das regras de movimentação, coleta de itens e progressão entre fases.

## 🎯 Objetivo acadêmico

O projeto tem como objetivo aplicar conceitos teóricos de Matemática Computacional na construção de uma aplicação interativa, demonstrando como estruturas matemáticas e algoritmos podem ser utilizados no desenvolvimento de jogos digitais.

## 👨‍💻 Autor

**Lucas Gabriel Dias Costa**
**João Guilherme Machado Ferreira**
**Luiz Henrique Cordeiro dos Santos **


Projeto acadêmico desenvolvido em Python.

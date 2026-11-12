# 🧩 Labirinto dos Enigmas

**Um jogo desenvolvido em Python que combina exploração de labirintos, desafios matemáticos e aplicação de algoritmos de busca e otimização de caminhos.**

## 📖 Sobre o projeto

O **Labirinto dos Enigmas** é um projeto acadêmico desenvolvido para a disciplina de **Matemática Computacional**, utilizando Python e a biblioteca Pygame.

O jogo apresenta labirintos com obstáculos, chaves, enigmas matemáticos e um portal que representa o destino final.

A proposta é demonstrar como conceitos matemáticos e computacionais podem ser aplicados em problemas de navegação, planejamento de rotas e otimização de caminhos.

O projeto possui dois modos principais: Modo Jogador e Modo BOT, permitindo explorar tanto a navegação controlada por uma pessoa quanto a resolução computacional do problema.

## 🎮 Modos de jogo

### 🧑 Modo Jogador

O jogador controla diretamente o personagem e precisa:

- Explorar o labirinto.
- Encontrar chaves espalhadas pelo mapa.
- Resolver enigmas matemáticos.
- Desviar de obstáculos e becos sem saída.
- Encontrar o portal para concluir cada fase.

A dificuldade aumenta progressivamente conforme o jogador avança.

### 🤖 Modo BOT

Um agente computacional é responsável por analisar o labirinto e planejar seu percurso.

O BOT deverá:

- Identificar os caminhos disponíveis.
- Localizar os objetivos obrigatórios.
- Coletar todas as chaves.
- Cumprir os requisitos dos enigmas.
- Encontrar uma rota até o portal.
- Buscar minimizar a distância total percorrida.

O modo BOT permite estudar e comparar diferentes estratégias de busca computacional.

## 🌎 Problema do mundo real

O projeto é inspirado em problemas de planejamento de rotas presentes na logística e no transporte de mercadorias.

Imagine uma transportadora que precisa realizar entregas em diferentes endereços de uma cidade. Para concluir o serviço de maneira eficiente, é necessário determinar a melhor sequência de visitas, considerando as distâncias entre os destinos e os caminhos disponíveis.

Uma rota mal planejada pode aumentar o percurso, o consumo de combustível e o tempo necessário para realizar todas as entregas.

O labirinto funciona como uma representação simplificada desse cenário:

- **Labirinto:** ambiente de deslocamento.
- **Paredes:** obstáculos ou caminhos bloqueados.
- **Chaves:** destinos obrigatórios.
- **Portal:** destino final.
- **BOT:** agente responsável pelo planejamento da rota.

## 🧠 Conceitos de Matemática Computacional

O projeto utiliza diferentes conceitos matemáticos e computacionais:

- **Matrizes:** representação do labirinto em uma estrutura bidimensional.
- **Grafos:** representação das posições acessíveis e suas conexões.
- **BFS (Busca em Largura):** exploração de caminhos por níveis.
- **A* (A-Star):** busca orientada por custo e estimativa de distância.
- **Heurísticas:** estimativa do custo restante até um objetivo.
- **Otimização de rotas:** planejamento da sequência de visitação de múltiplos objetivos.

### BFS — Breadth-First Search

Explora os vértices de um grafo por níveis e encontra o caminho com menor quantidade de movimentos quando todos os movimentos possuem o mesmo custo.

### A* — A-Star

Utiliza uma função de avaliação que combina o custo já percorrido com uma estimativa da distância restante:

\[
f(n) = g(n) + h(n)
\]

Onde:

- `g(n)`: custo acumulado do caminho.
- `h(n)`: estimativa do custo restante.
- `f(n)`: custo estimado total.

Uma das heurísticas que pode ser utilizada é a distância Manhattan, adequada para ambientes com movimentação horizontal e vertical.

## 📊 Análise de desempenho

A comparação das estratégias de navegação considera métricas como:

| Métrica | Descrição |
|---|---|
| Distância percorrida | Total de movimentos realizados |
| Posições exploradas | Quantidade de posições analisadas |
| Tempo de processamento | Tempo gasto pelo algoritmo para encontrar a solução |
| Eficiência da rota | Qualidade do percurso encontrado |

Essas métricas permitem analisar o comportamento dos algoritmos diante de labirintos com diferentes dimensões, obstáculos e quantidades de objetivos.

## 🛠️ Tecnologias utilizadas

- **Python 3:** desenvolvimento da lógica do jogo e dos algoritmos.
- **Pygame:** criação da interface gráfica, movimentação dos personagens e interação com o usuário.

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Lucas-Dias07/Trabalho_A3.git
```

### 2. Entre na pasta do projeto

```bash
cd Trabalho_A3
```

### 3. Instale a biblioteca Pygame

```bash
pip install pygame
```

### 4. Execute o jogo

```bash
python jogo.py
```

## 👥 Integrantes

- **Lucas Gabriel Dias Costa - 326124418**
- **João Guilherme Machado Ferreira  - 326128074**
- **Luiz Henrique Cordeiro dos Santos - 326122345**

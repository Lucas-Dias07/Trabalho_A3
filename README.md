# 🧩 Labirinto dos Enigmas

**Um projeto de Matemática Computacional que combina exploração de labirintos, desafios matemáticos e algoritmos de busca e otimização de caminhos.**

## 📖 Sobre o projeto

O **Labirinto dos Enigmas** é um jogo desenvolvido em Python com a biblioteca Pygame, cujo objetivo é explorar ambientes com obstáculos, coletar chaves, resolver desafios matemáticos e encontrar a saída.

O projeto busca demonstrar, de maneira prática e interativa, como conceitos de Matemática Computacional podem ser aplicados em problemas de navegação, planejamento de rotas e otimização de caminhos.

A proposta é inspirada em situações do mundo real, como o planejamento de entregas em diferentes endereços, a movimentação de robôs autônomos e a organização de trajetos em ambientes complexos.

## 🎮 Modos de jogo

### 🧑 Modo Jogador

O jogador controla diretamente o personagem e precisa:

- Explorar o labirinto.
- Encontrar chaves espalhadas pelo mapa.
- Resolver enigmas matemáticos.
- Evitar obstáculos e becos sem saída.
- Encontrar o portal para concluir cada fase.

A dificuldade aumenta progressivamente conforme o jogador avança.

### 🤖 Modo BOT

Um agente computacional é responsável por analisar o labirinto e planejar seu percurso.

O BOT precisa:

- Identificar os caminhos disponíveis.
- Localizar os objetivos obrigatórios.
- Coletar todas as chaves.
- Cumprir os requisitos dos enigmas.
- Encontrar uma rota até o portal.
- Buscar minimizar a distância total percorrida.

O modo BOT também permite estudar e comparar diferentes estratégias de busca computacional.

## 🧠 Conceitos de Matemática Computacional

O projeto utiliza conceitos matemáticos e computacionais para representar e solucionar o problema de navegação.

**Principais conceitos:**

- Matrizes: representação do labirinto em uma estrutura bidimensional.
- Grafos: representação das posições acessíveis e suas conexões.
- Busca em largura (BFS): exploração de caminhos por níveis.
- Busca A* (A-Star): busca orientada por custo e estimativa de distância.
- Heurísticas: estimativa do custo restante até um objetivo.
- Otimização de rotas: planejamento da sequência de visitação de múltiplos objetivos.

### Algoritmos de busca

**BFS — Breadth-First Search**

Explora os vértices de um grafo por níveis e encontra o caminho com menor quantidade de movimentos quando todos os movimentos possuem o mesmo custo.

**A* — A-Star**

Utiliza uma função de avaliação que combina o custo já percorrido com uma estimativa da distância restante:

\[
f(n) = g(n) + h(n)
\]

Onde:

- `g(n)`: custo acumulado do caminho.
- `h(n)`: estimativa do custo restante.
- `f(n)`: custo estimado total.

Uma das heurísticas utilizadas em ambientes com movimentação horizontal e vertical é a distância Manhattan.

## 🌎 Aplicação no mundo real

O problema abordado pelo projeto possui relação com o planejamento de rotas de entrega.

Imagine uma transportadora que precisa realizar entregas em vários endereços antes de retornar à base ou concluir seu percurso.

Nesse cenário, é necessário considerar:

- Distância entre os destinos.
- Obstáculos e caminhos disponíveis.
- Ordem de visitação dos endereços.
- Distância total percorrida.
- Tempo necessário para concluir as entregas.

O labirinto funciona como uma representação simplificada desse ambiente, enquanto as chaves representam os destinos obrigatórios e o portal representa o destino final.

## 📊 Análise de desempenho

O projeto propõe comparar o desempenho dos algoritmos por meio de diferentes métricas:

| Métrica | Descrição |
|---|---|
| Distância percorrida | Total de movimentos realizados |
| Posições exploradas | Quantidade de posições analisadas |
| Tempo de processamento | Tempo gasto pelo algoritmo para encontrar a solução |
| Eficiência da rota | Qualidade do percurso encontrado |

A análise permite observar como diferentes estratégias se comportam diante de labirintos com diferentes dimensões, obstáculos e quantidades de objetivos.

## 🛠️ Tecnologias utilizadas

- **Python 3:** desenvolvimento da lógica e dos algoritmos.
- **Pygame:** criação da interface gráfica e interação com o jogo.

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Lucas-Dias07/matematica-computacional.git
```

### 2. Entre na pasta do projeto

```bash
cd matematica-computacional
```

### 3. Instale a biblioteca Pygame

```bash
pip install pygame
```

### 4. Execute o jogo

Utilize o comando correspondente ao arquivo principal:

```bash
python Labirinto_dos_Enigmas_BOT.py
```

## 👥 Integrantes

- **Lucas Gabriel Dias Costa**
- **João Guilherme Machado Ferreira**
- **Luiz Henrique Cordeiro dos Santos**

## 🎓 Disciplina

Projeto desenvolvido para a disciplina de **Matemática Computacional**, com foco na aplicação de modelagem matemática, algoritmos de busca e otimização.

---

**Labirinto dos Enigmas — Explorando caminhos, resolvendo problemas e aplicando algoritmos.**

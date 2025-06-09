# 🤖 Robô Gamer com Visão Computacional (Dino Game)

Bot em Python que utiliza Visão Computacional para jogar o "Dino Game" do navegador de forma completamente autônoma. O robô é capaz de analisar a tela em tempo real para identificar e desviar de obstáculos, além de reiniciar o jogo automaticamente após uma derrota, permitindo sessões de jogo contínuas.

Este repositório contém o script principal do robô (`robo_gamer.py`) e um script utilitário (`descobrir_coordenadas.py`) para auxiliar na calibração inicial.

---

### ⚙️ Funcionalidades Principais

* ✅ **Detecção de Obstáculos:** Utiliza processamento de imagem com OpenCV para identificar cactos e pássaros em uma área de detecção ("sensor") à frente do dinossauro.
* ✅ **Ação Autônoma:** Simula o pressionamento da tecla "espaço" com PyAutoGUI para pular os obstáculos com precisão.
* ✅ **Reinício Automático:** Usa a técnica de *Template Matching* do OpenCV para reconhecer o botão de "Game Over" e reiniciar o jogo de forma autônoma.
* ✅ **Captura de Tela Otimizada:** Utiliza a biblioteca `mss` para captura de tela de alta performance, permitindo uma análise fluida e em tempo real.

---

### 🛠️ Tecnologias Utilizadas

* **Python 3**
* **OpenCV:** Para todo o processamento de imagem, conversão de cores e template matching.
* **MSS:** Para captura de tela de alta performance.
* **PyAutoGUI:** Para a automação da entrada de teclado.
* **NumPy:** Para manipulação eficiente dos arrays de pixels das imagens.

---

### 🚀 Como Executar o Projeto

**Pré-requisitos:**
* Python 3.x instalado.

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/CarlosDevZera/Robo_gamer.git
    cd Robo_gamer
    ```
2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    # No Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    * (Certifique-se de ter um arquivo `requirements.txt`. Para criá-lo, rode `pip freeze > requirements.txt` no seu terminal).
    ```bash
    pip install -r requirements.txt
    ```
4.  **Passo Essencial: Calibração para a sua Tela**
    * A eficácia do robô depende de uma calibração precisa para a sua resolução de tela e posição da janela do jogo. Para isso, utilize o script auxiliar:
    ```bash
    python descobrir_coordenadas.py
    ```
    * O terminal começará a exibir a posição X e Y do seu mouse.
    * **Para a variável `MONITOR`:**
        * a. Posicione o mouse no canto superior esquerdo da área do jogo e anote `X` (será seu `left`) e `Y` (será seu `top`).
        * b. Posicione o mouse no canto inferior direito da área do jogo e anote `X_final` e `Y_final`.
        * c. Calcule: `width = X_final - left` e `height = Y_final - top`.
    * **Para a variável `AREA_DE_DETECAO`:** Repita o processo para o pequeno retângulo "sensor" que deve ficar à frente do dinossauro.
    * **Atualize** os valores no topo do arquivo `robo_gamer.py` com as coordenadas que você encontrou.

5.  **Execute como Administrador:**
    * Este script precisa controlar o navegador. Por questões de segurança do Windows, é necessário executá-lo com privilégios de administrador.
    * Abra seu terminal ou IDE clicando com o botão direito e selecionando **"Executar como administrador"**.

6.  **Inicie o robô:**
    ```bash
    python robo_gamer.py
    ```
    * Você terá 2 segundos para clicar na janela do jogo e dar o foco a ela. Depois, é só assistir!

---

### 🧠 Desafios e Aprendizados

Este projeto foi uma jornada completa de depuração e resolução de problemas do mundo real. Os principais desafios superados foram:

* **Calibração de Sensores:** Encontrar a posição e o tamanho exatos da `AREA_DE_DETECAO` para evitar falsos positivos com o chão do jogo.
* **Reinício Autônomo:** Implementar o reconhecimento do botão de "Game Over" com a técnica de Template Matching foi um desafio interessante para criar um ciclo de jogo 100% autônomo, sem necessidade de intervenção humana.
* **Detecção Robusta de Obstáculos:** A detecção de um cacto não podia ser apenas a checagem de um único pixel, pois isso seria muito frágil. O desafio foi criar um método mais robusto. A solução implementada foi definir uma "área de detecção" (um retângulo) à frente do dinossauro e aplicar uma pequena pipeline de processamento de imagem do OpenCV.

---

### 👨‍💻 Autor

Feito por **Carlos**.

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eucarlosalberto/)


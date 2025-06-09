import cv2
import numpy as np
import mss
import time
import pyautogui

# Área de captura da tela
MONITOR = {'top': 136, 'left': 146, 'width': 832, 'height': 450}

# Área de detecção de obstáculos
AREA_DE_DETECAO = (185, 250, 260, 280)

# Sensibilidade da detecção de obstáculos
THRESHOLD_PIXELS_ESCUROS = 10

# Configurações do reinício
CAMINHO_TEMPLATE_RESTART = 'D:/PyProjetos/pjt008/robo_gamer/img/1.PNG'
THRESHOLD_REINICIO = 0.8

def carregar_template(caminho_arquivo):
    """Tenta carregar a imagem do template de reinício."""
    try:
        template = cv2.imread(caminho_arquivo, 0)
        if template is None:
            raise FileNotFoundError("O arquivo de imagem não foi encontrado ou está corrompido.")
        print("Template do botão de recomeçar carregado com sucesso.")
        return template
    except Exception as e:
        print(f"ERRO ao carregar a imagem do botão: {e}")
        return None

def checar_game_over(imagem_cinza, template):
    """Verifica se a tela de 'Game Over' está visível."""
    if template is None:
        return False

    res = cv2.matchTemplate(imagem_cinza, template, cv2.TM_CCOEFF_NORMED)
    if np.max(res) >= THRESHOLD_REINICIO:
        print("Tela de 'Game Over' detectada. Reiniciando...")
        pyautogui.press('space')
        time.sleep(1)
        return True
    return False

def checar_obstaculo(imagem_cinza):
    """Verifica se há um obstáculo na área de detecção."""
    x1, y1, x2, y2 = AREA_DE_DETECAO
    area_obstaculo = imagem_cinza[y1:y2, x1:x2]

    _, area_preto_e_branco = cv2.threshold(area_obstaculo, 100, 255, cv2.THRESH_BINARY_INV)
    pixels_escuros = cv2.countNonZero(area_preto_e_branco)

    if pixels_escuros > THRESHOLD_PIXELS_ESCUROS:
        pyautogui.press('space')
        print(f"Pulo! (Detectados {pixels_escuros} pixels de obstáculo)")

template_restart = carregar_template(CAMINHO_TEMPLATE_RESTART)

print("Iniciando o robô... Pressione Ctrl+C no terminal para sair.")
time.sleep(2)
pyautogui.press('space')

try:
    with mss.mss() as sct:
        while True:
            img_color = np.array(sct.grab(MONITOR))
            img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

            if checar_game_over(img_gray, template_restart):
                continue

            checar_obstaculo(img_gray)

except KeyboardInterrupt:
    print("\nRobô desligado.")
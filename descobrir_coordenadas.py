import pyautogui
import time

print("Iniciando o detetive de coordenadas...")
print("Mova o mouse para os cantos da área do jogo para descobrir os valores.")
print("Pressione Ctrl+C no terminal para parar o programa.")

try:
    # Loop infinito para mostrar a posição do mouse continuamente
    while True:
        # Pega a posição atual do mouse (coordenadas X e Y)
        x, y = pyautogui.position()

        # Formata a string para exibição
        posicao_str = f"X: {x:4d} Y: {y:4d}"

        # PLANO B: Imprime uma nova linha a cada vez.
        # Isto é garantido de funcionar em 100% dos casos.
        print(posicao_str)

        # Uma pequena pausa para não sobrecarregar
        time.sleep(0.1)

except KeyboardInterrupt:
    # Mensagem para quando você parar o programa
    print("\nPrograma finalizado.")
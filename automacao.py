import keyboard
import time
import random

# Alterna a ordem das teclas
alternar = False

def aperta_ad():
    global alternar

    if alternar:
        keyboard.press('a')
        time.sleep(0.005)
        keyboard.press('d')
    else:
        keyboard.press('d')
        time.sleep(0.005)
        keyboard.press('a')

    time.sleep(0.08)

    if alternar:
        keyboard.release('d')
        time.sleep(0.005)
        keyboard.release('a')
    else:
        keyboard.release('a')
        time.sleep(0.005)
        keyboard.release('d')

    alternar = not alternar
    print("A + D")

def aperta_e():
    keyboard.press_and_release('e')
    print("E")

print("Você tem 3 segundos para focar a janela...")
time.sleep(3)

while True:
    # A + D
    aperta_ad()

    time.sleep(random.uniform(0.15, 0.35))

    # E
    aperta_e()

    time.sleep(random.uniform(0.15, 0.35))

    # A + D
    aperta_ad()

    time.sleep(random.uniform(0.15, 0.35))

    # E
    aperta_e()

    print("Aguardando 5 minutos...")
    time.sleep(300)
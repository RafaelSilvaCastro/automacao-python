# Achar o ponto x e y do computador para ser clicado

import pyautogui
import time

time.sleep(5)
print(pyautogui.position())

# funcionamento do scrool 
# - vai pra baixo / + vai pra cima 
pyautogui.scroll(250)

# saber o nome das teclas
#print(pyautogui.KEYBOARD_KEYS)
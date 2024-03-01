#IMPORTANDO BIBLIOTECA
import pyautogui
import time

#clicar -> pyautogui.click
#escrever -> pyautogui.write
#apertar tecla -> pyautogui.press
#apertar -> pyautogui.hotkey
#scroll -> pyautogui.scroll

pyautogui.PAUSE = 1
#aperta a tecla windows (comand + barra de espaço)
pyautogui.press("win")
#digita o nome do programa (chrome)
pyautogui.write("main.html")
#aperta enter
pyautogui.press("enter")

#espera 5 segundos
pyautogui.sleep(3)

#digita o link - escreve o link - pressiona enter
link = "file:///C:/Users/Marcia/Desktop/curso%20python/automacao%20py/main.html"
pyautogui.write(link)
pyautogui.press("enter")

#passo 2 = fazer login
pyautogui.sleep(3)
pyautogui.click(x=710, y=457)

#digitar email
pyautogui.write("ExemplodeEmail@gmail.com")

#passar para o campo de senha
pyautogui.press("tab")

#senha - enter
pyautogui.write("123abc")
pyautogui.press("enter")
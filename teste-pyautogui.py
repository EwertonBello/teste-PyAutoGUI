# o programa foi testado com o objetivo selecionar a barra de pesquisa do browser, digitar "Arroz" e pressionar enter para pesquisar.
import pyautogui
# print(pyautogui.position()) Saída: x=257, y=52. método position() utilizado para exibir a localização atual do ponteiro do mouse.

pyautogui.click(257, 52)#Método click para efetuar um click do mouse na localização informada.
pyautogui.typewrite("Arroz")#Método typewrite para controlar o teclado e digitar os argumentos informados no método.
pyautogui.typewrite(["enter"])#Método typewrite para controlar o teclado e pressionar a tecla "enter", para isso informar o nome da tecla entre [].

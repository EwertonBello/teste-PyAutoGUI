import pyautogui

pesquisa = pyautogui.prompt('Digite sua pesquisa')
pyautogui.click(257, 52)
pyautogui.typewrite(pesquisa)
pyautogui.press("enter")

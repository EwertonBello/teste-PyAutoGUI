import pyautogui

# pyautogui.click(257, 52)
# pyautogui.typewrite("Arroz")
# pyautogui.typewrite(["enter"])

# print(pyautogui.size())# (width=1920, height=1080)
x, y = pyautogui.size()
# 200 --- 100%
# 15  ---  x%
# x% = (15*100)/200

# x --- 100%
# 88 --- valorx%
# valorx% = (88*100%)/x
# 4,58%

# y --- 100%
# 103 --- valory%
# valory% = (103*100%)/y
# 9,54%

# print(pyautogui.position())# (x=88, y=103)

pyautogui.click((4.58/100)*x, (9.54/100)*y)
pyautogui.typewrite("EwertonBello")
pyautogui.typewrite(["enter"])

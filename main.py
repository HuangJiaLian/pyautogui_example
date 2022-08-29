import pyautogui, time

def extendSession():
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX, currentMouseY)
    iconX, iconY = 778, 10
    pyautogui.click(iconX, iconY)
    pyautogui.move(0, 100)
    time.sleep(0.2)
    pyautogui.move(220, 0)
    time.sleep(0.2)
    pyautogui.move(0, 110)
    pyautogui.click()
    pyautogui.moveTo(currentMouseX, currentMouseY)

while True:
    extendSession()
    #time.sleep(10*60)
    time.sleep(10)

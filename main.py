#!/usr/bin/env python
import pyautogui, time

def extendSession(x, y):
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(x, y)
    pyautogui.move(0, 100)
    time.sleep(0.2)
    pyautogui.move(220, 0)
    time.sleep(0.2)
    pyautogui.move(0, 110)
    pyautogui.click()
    pyautogui.moveTo(currentMouseX, currentMouseY)
    print('Extend session triggerd')


def main():
    print('Put the mouse curser to the icon first:')
    countNum = 5
    for i in range(countNum):
        print('Counting down {} s ...'.format(countNum-i))
        time.sleep(1)
    iconX, iconY = pyautogui.position()
    while True:
        extendSession(iconX, iconY)
        time.sleep(10*60)

if __name__ == '__main__':
    main()

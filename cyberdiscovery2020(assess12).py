from pynput.mouse import Button, Controller
import keyboard
import time

# ==============================================

mouse = Controller()

print(mouse.position)
# ==============================================

def button1():
    mouse.position = (501, 352)
    mouse.click(Button.left, 1)

def button2():
    mouse.position = (618, 347)
    mouse.click(Button.left, 1)

def button3():
    mouse.position = (756, 351)
    mouse.click(Button.left, 1)

def button4():
    mouse.position = (500, 475)
    mouse.click(Button.left, 1)

def button5():
    mouse.position = (632, 482)
    mouse.click(Button.left, 1)

def button6():
    mouse.position = (760, 479)
    mouse.click(Button.left, 1)

def button7():
    mouse.position = (500, 601)
    mouse.click(Button.left, 1)

def button8():
    mouse.position = (627, 598)
    mouse.click(Button.left, 1)

def button9():
    mouse.position = (759, 603)
    mouse.click(Button.left, 1)

def button0():
    mouse.position = (645, 720)
    mouse.click(Button.left, 1)

def main():

    button3()
    button9()
    button8()
    button6()
    button2()
    button9()
    button8()
    button4()
    button7()
    button6()
    button4()
    button3()
    button8()
    button0()
    button7()
    button3()

main()

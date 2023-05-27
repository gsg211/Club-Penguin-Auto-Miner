import pyautogui as auto
import time
import random
import keyboard
from tkinter import *
import threading
import os

# coordinates for the mining rectangle
x1 = 0
x2 = 0
y1 = 0
y2 = 0

penguin_card = 0


def mine():
    global penguin_card
    auto.click(random.randint(x1, x2), random.randint(y1, y2), clicks=1)
    check_penguin()
    if penguin_card == 0:
        time.sleep(3.5)
        auto.press('d')
        time.sleep(1)
        auto.keyUp('d')
        time.sleep(17)


# there are chances that the bot will click another penguin
# to check if a penguin card is obstructing the screen and to close it the bot uses this function
def check_penguin():
    global penguin_card
    try:
        xlocation = auto.locateOnScreen('xspot.png', confidence=0.8)
        xpoint = auto.center(xlocation)
        print(xpoint.x, xpoint.y)
        if xpoint:
            print(xpoint.x, xpoint.y)
            auto.click(xpoint.x, xpoint.y, clicks=1)
            time.sleep(0.25)
            penguin_card = 1
    except TypeError:
        print("not found")


# for clicking the discover treasure ability when having a gold or brown puffle
def check_puffle_gold():
    try:
        xlocation = auto.locateOnScreen('pufflespot.png', confidence=0.8)
        xpoint = auto.center(xlocation)
        print(xpoint.x, xpoint.y)
        if xpoint:
            print(xpoint.x, xpoint.y)
            auto.click(xpoint.x, xpoint.y, clicks=1)
            time.sleep(0.1)
    except TypeError:
        print("not found")
    try:
        xlocation = auto.locateOnScreen('moneyspot.png', confidence=0.9)
        xpoint = auto.center(xlocation)
        print(xpoint.x, xpoint.y)
        if xpoint:
            print(xpoint.x, xpoint.y)
            auto.click(xpoint.x, xpoint.y, clicks=1)
            time.sleep(0.1)
    except TypeError:
        print("not found")


def check_puffle_brown():
    try:
        xlocation = auto.locateOnScreen('brownpuffle.png', confidence=0.8)
        xpoint = auto.center(xlocation)
        print(xpoint.x, xpoint.y)
        if xpoint:
            print(xpoint.x, xpoint.y)
            auto.click(xpoint.x, xpoint.y, clicks=1)
            time.sleep(0.1)
    except TypeError:
        print("not found")
    try:
        xlocation = auto.locateOnScreen('moneyspot.png', confidence=0.9)
        xpoint = auto.center(xlocation)
        print(xpoint.x, xpoint.y)
        if xpoint:
            print(xpoint.x, xpoint.y)
            auto.click(xpoint.x, xpoint.y, clicks=1)
            time.sleep(0.1)
    except TypeError:
        print("not found")


# functions to set the boundaris of the mining rectangle
def get_location_x1():
    global x1
    while 1:
        if keyboard.is_pressed('e'):
            x1 = auto.position().x
            print(x1)
            break


def get_location_x2():
    global x2
    while 1:
        if keyboard.is_pressed('e'):
            x2 = auto.position().x
            print(x2)
            break


def get_location_y1():
    global y1
    while 1:
        if keyboard.is_pressed('e'):
            y1 = auto.position().y
            print(y1)
            break


def get_location_y2():
    global y2
    while 1:
        if keyboard.is_pressed('e'):
            y2 = auto.position().y
            print(y2)
            break


# the m
def start_mining():
    global penguin_card
    time.sleep(1)
    while 1:
        check_penguin()
        penguin_card = 0
        time.sleep(0.2)
        check_puffle_gold()
        check_puffle_brown()
        time.sleep(0.2)
        mine()


# threads for the button functions
def x1btn():
    thread = threading.Thread(target=get_location_x1())
    thread.start()


def x2btn():
    thread = threading.Thread(target=get_location_x2())
    thread.start()


def y1btn():
    thread = threading.Thread(target=get_location_y1())
    thread.start()


def y2btn():
    thread = threading.Thread(target=get_location_y2())
    thread.start()


def mine_btn():
    thread = threading.Thread(target=start_mining)
    thread.start()


def exit_program():
    quit()


def exit_btn():
    thread = threading.Thread(target=os._exit(0))
    thread.start()


if __name__ == '__main__':
    win = Tk()
    win.geometry("350x500")
    win.title("Club penguin auto miner")
    Label(win, text="Select a button then", font=("Calibri", 14)).pack(pady=10)
    Label(win, text="press e to select boundary", font=("Calibri", 14)).pack(pady=10)
    Label(win, text="After that, press mine to start", font=("Calibri", 14)).pack(pady=10)
    Button(win, text="left position", font=("Calibri", 12, "bold"), command=x1btn).pack(pady=10)
    Button(win, text="right position", font=("Calibri", 14, "bold"), command=x2btn).pack(pady=10)
    Button(win, text="top position", font=("Calibri", 14, "bold"), command=y1btn).pack(pady=10)
    Button(win, text="bottom position", font=("Calibri", 14, "bold"), command=y2btn).pack(pady=10)
    Button(win, text="mine", font=("Calibri", 14, "bold"), command=mine_btn).pack(pady=10)
    Button(win, text="close", font=("Calibri", 14, "bold"), command=exit_btn).pack(pady=10)
    win.mainloop()

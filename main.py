import time
import keyboard
import pyautogui
import threading

firstblock = [1400, 700]
secondblock = [1540, 700]
positionfist = [1000, 1350]
positionmeg = [1190, 1350]
blockbreaknumber = 9


def infiniteloop1():
    while True:
        global stop_thread
        pyautogui.click(positionmeg[0], positionmeg[1])
        time.sleep(0.1)
        pyautogui.click(firstblock[0], firstblock[1])
        time.sleep(0.1)
        pyautogui.click(secondblock[0], secondblock[1])
        time.sleep(0.1)
        pyautogui.click(positionfist[0], positionfist[1])
        time.sleep(0.1)
        for s in range(blockbreaknumber):
            pyautogui.click(firstblock[0], firstblock[1])
            time.sleep(0.1)
        time.sleep(0.1)
        for q in range(blockbreaknumber):
            pyautogui.click(secondblock[0], secondblock[1])
            time.sleep(0.1)
        if stop_thread:
            break


def infiniteloop2():
    while True:
        if keyboard.read_key() == "p":
            global stop_thread
            stop_thread = True
            print("Program killed")
            break


stop_thread = False
thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()

# first block = 1400:700
# second block = 1540:700
# position fist = 1000:1350
# position meg = 1190:1350

# while(True):
#     print(pyautogui.position())
#     time.sleep(0.5)

import pynput
import time
import random
import tkinter
from tkinter import messagebox
from pynput.mouse import Button, Controller

root = tkinter.Tk()
root.withdraw()
#* Colocando o mouse como controle
mouse = Controller();

messagebox.showinfo("Danger!", "Your computer has been infected!")
#* Descobrir a atual posição do mouse

print("Posição atual: " + str(mouse.position));
for count in range(100):
    print(time.ctime())
    mouse.move(random.randint(-10,10), random.randint(-10,10));
    time.sleep(0.0006)
for count in range(100):
    print(time.ctime())
    mouse.move(random.randint(-50,50), random.randint(-50,50));
    time.sleep(0.0006)
for count in range(100):
    print(time.ctime())
    mouse.move(random.randint(-100,100), random.randint(-100,100));
    time.sleep(0.0006)
from threading import Thread, Event
import tkinter as tk
import tkinter.ttk as ttk
import time

event = Event()

def loop(event : Event):
    while True:
        print(cmb.get())
        if event.is_set():
            break

def create_thread():
    x = Thread(target=create_thread, args=(event))
    x.start()

root = tk.Tk()
root.geometry("800x600")

btn = tk.Button(root, text="thread", command=create_thread)
btn.pack()

cmb = ttk.Combobox(root, values=["Escolha", 1, 2, 3])
cmb.current(0)
cmb.pack()

stop = tk.Button(root, text="stop", command=lambda : event.set())
stop.pack()

root.mainloop(s)
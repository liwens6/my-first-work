import tkinter as tk
windows = tk.Tk()
windows.title("helloworld")
windows.geometry("400x400")
l = tk.Label(windows, text="hello world", bg="green",font=("Arial",12),width = 15,height = 2)
l.pack()
windows.mainloop
oh,shit
import tkinter as tk

window = tk.Tk()
window.title('helloworld')
window.geometry('400x400')

l = tk.Label(window, text='fuck u', bg="green",font=("Arial",12),width = 15,height = 2)
l.pack()

window.mainloop
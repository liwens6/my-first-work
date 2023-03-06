import tkinter as tk
windows = tk.Tk()
windows.title("helloworld")
windows.geometry("400x400")
var = tk.StringVar()
l = tk.Label(windows, text="hello world", bg="green",font=("Arial",12),width = 15,height = 2)
l.pack()

is_Hidden= False
def hidden_me():
    global is_Hidden
    if is_Hidden == False:
        is_Hidden = True
        var.set('click me and hidden')
    else:
        is_Hidden = False
        var.set('')
var1 = tk.StringVar()
var1.set('hidden')
b = tk.Button(windows,textvariable=var1,width = 12,height = 2,command = hidden_me)
b.pack()
windows.mainloop
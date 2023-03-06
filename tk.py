import tkinter as tk
window = tk.Tk()
window.title('my first window')
window.geometry('200x100')
var = tk.StringVar()
l = tk.Label(window,textvariable=var,bg = 'green',font=('Arial',12),width = 25,height=4)
l.pack()
is_Hidden = False
def hidden_me():
    global is_Hidden
    if is_Hidden ==False:
        is_Hidden = True
        var.set('clivk me and hidden')
    else:
        is_Hidden = False
        var.set('')

var1 = tk.StringVar()
var1.set('hidden')
b = tk.Button(window,textvariable=var1,width=12,height=2,command=hidden_me)
b.pack()
window.mainloop()
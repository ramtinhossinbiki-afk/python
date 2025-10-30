import tkinter as tk
import json as j
import datetime
import turtle
import time

x = datetime.datetime.now()
def n():
    screen = turtle.Screen()
    screen.bgcolor("light blue")
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pensize(3)
    pen.speed(0.1)
    def write_animated(text, start_x, start_y, spacing=40):
        pen.penup()
        x = start_x
        for char in text:
            pen.goto(x, start_y)
            pen.pendown()
            pen.write(char, font=("Arial", 36, "bold"))
            pen.penup()
            x += spacing
            time.sleep(0.1)
    write_animated("THIS POROJE", -180, 50)
    write_animated("WAS",-180,8)
    write_animated("MADE",-180,-34)
    write_animated("IN",-180,-76)
    write_animated("RAM C",-180,-118)


# تنظیمات اولیه
    
# تابع cursor پویا
def add_cursor_binding(widget):
    global sa, ee, till, c, f, g,gg,x
    widget.bind("<Enter>", lambda e: widget.configure(cursor="circle"))
    widget.bind("<Leave>", lambda e: widget.configure(cursor="watch"))

def b():
    global sa, ee, till, c, f, g,gg,x,h,n
    if isinstance(c, tk.Widget):
        c.destroy()
    if isinstance(sa, tk.Widget):
        sa.destroy()
    f = tk.Label(till, text="توليد شده توسط شرکت رام اچ بي", bg=gg, fg="black", font=("Arial", 40))
    f.pack()
    g = tk.Button(till, text="برگشت", bg=gg, fg="black", font=("Arial", 40), command=a)
    g.pack()
    add_cursor_binding(g)    
def e():
    global sa, ee, till, c, f, g,gg,x,h,n
    if isinstance(c, tk.Widget):
        c.destroy()
    if isinstance(g, tk.Widget):
        g.destroy()
    if isinstance(sa, tk.Widget):
        sa.destroy()
    if isinstance(sa, tk.Widget):
        sa.destroy()
    if isinstance(sa, tk.Widget):
        sa.destroy()    
    ee = tk.Button(till, text="برگشت", bg=gg, fg="black", font=("Arial", 40), command=a)
    ee.pack()
    add_cursor_binding(ee)

def a():
    global sa, ee, till, c, f,s,gg,x,h,n
    for w in [ee, f, g]:
        if isinstance(w, tk.Widget):
            w.destroy()
        if isinstance(h, tk.Widget):
            h.destroy()
    sa = tk.Button(till, text="سلام", bg=gg, fg="black", font=("Arial", 40), command=e)
    sa.pack(pady=0)
    dd = tk.Button(till, text="سلام", bg=gg, fg="black", font=("Arial", 40), command=n)
    dd.pack(pady=0)
    c = tk.Button(till, text=" منو", bg=gg, fg="black", font=("Arial", 40), command=b)
    c.pack(pady = 100)
    h = tk.Label(till, text=x, bg=gg, fg="black", font=("Arial", 40))
    h.pack(pady=0)
    add_cursor_binding(sa)
    add_cursor_binding(c)

sa = None
ee = None
c = None
f = None
g = None
h = None
gg = "#e9f8ff"
till = tk.Tk()
till.geometry("800x800")
menu = tk.Menu(till)
till.config(menu=menu)
file_menu = tk.Menu(menu)
till.configure(bg=gg)
menu.add_cascade(label="رنگ صفحه", menu=file_menu)
file_menu.add_command(label="آبي")
file_menu.add_command(label="سياه")
file_menu.add_command(label="قرمز")
men = tk.Menu(till)
till.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="خروج", menu=file_menu)
file_menu.add_command(label="خروج",accelerator="Ctrl+Q", command=till.destroy)
a()
till.mainloop()

import tkinter as tk
import tkinter.messagebox
import random

bg = tk.Tk()
bg.title('Next')
bg.geometry('250x130')

new_one = tk.StringVar()
new_one.set('')
new_two = tk.StringVar()
new_two.set('')

def code():
    mun1 = new_one.get()
    mun2 = new_two.get()
    end = random.randint(1,2)
    if end == 1:
        tkinter.messagebox.showinfo(title = "你的计划是", message = mun1)    
    else:
        tkinter.messagebox.showinfo(title = "你的计划是", message = mun2)
def no():
    new_one.set('')
    new_two.set('')
def _quit():
    bg.quit()
    bg.destroy()

laone = tk.Label(bg, text = "计划一：", width = 80)
latwo = tk.Label(bg, text = "计划二：", width = 80)

enone = tk.Entry(bg, width = 100, textvariable = new_one)
entwo = tk.Entry(bg, width = 100, textvariable = new_two)

bu_y = tk.Button(bg, text = "确定", command = code)
bu_n = tk.Button(bg, text = "重置", command = no)
bu_q = tk.Button(bg, text = "退出", command = _quit)

laone.place(x = 20, y = 10, width = 80, height = 20)
latwo.place(x = 20, y = 40, width = 80, height = 20)
enone.place(x = 120, y = 10, width = 80, height = 20)
entwo.place(x = 120, y = 40, width = 80, height = 20)
bu_y.place(x = 30, y = 80, width = 50, height = 20)
bu_n.place(x = 100, y = 80, width = 50, height = 20)
bu_q.place(x = 170, y = 80, width = 50, height = 20)

bg.mainloop()
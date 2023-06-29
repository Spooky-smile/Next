#add
import tkinter as tk
import random
#Down
bg = tk.Tk()
bg.title('Next')
bg.geometry('250x150')
#None
new_one = tk.StringVar()
new_one.set('')
new_two = tk.StringVar()
new_two.set('')
#Out
plan = tk.Label(bg, text = '计划输出处', fg = 'grey')
#Do
def code(mun1, mun2):
    end = random.randint(1,2)
    if end == 1:
        plan.config(text = f'你的计划是 {mun1}', fg = 'black')    
    else:
        plan.config(text = f'你的计划是 {mun2}', fg = 'black')
def no():
    new_one.set('')
    new_two.set('')
def qu():
    bg.quit()
    bg.destroy()
#Out_where
laone = tk.Label(bg, text = '计划一：', width = 80)
latwo = tk.Label(bg, text = '计划二：', width = 80)
#In
enone = tk.Entry(bg, width = 100, textvariable = new_one)
entwo = tk.Entry(bg, width = 100, textvariable = new_two)
#Do_what
bu_y = tk.Button(bg, text = '确定',
                 command = lambda:code(enone.get(), entwo.get()))
bu_n = tk.Button(bg, text = '重置', command = no)
bu_q = tk.Button(bg, text = '退出', command = qu)
#Down_where
plan.place(x = 20, y = 10, height = 20)
laone.place(x = 20, y = 40, width = 80, height = 20)
latwo.place(x = 20, y = 80, width = 80, height = 20)
enone.place(x = 120, y = 40, width = 80, height = 20)
entwo.place(x = 120, y = 80, width = 80, height = 20)
bu_y.place(x = 170, y = 120, width = 50, height = 20)
bu_n.place(x = 100, y = 120, width = 50, height = 20)
bu_q.place(x = 30, y = 120, width = 50, height = 20)
#Top
bg.mainloop()
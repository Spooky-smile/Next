#Head
import tkinter as tk
import random
#Start
bg = tk.Tk()
bg.title('Next')
bg.geometry('320x250')
#None
new_one = tk.StringVar()
new_one.set('')
new_two = tk.StringVar()
new_two.set('')
#Out
plan = tk.Label(bg, text = '计划输出处', fg = 'grey')
#WorkCode
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
#In_What
lab_one = tk.Label(bg, text = '计划1:', width = 80)
lab_two = tk.Label(bg, text = '计划2:', width = 80)
#In
ent_one = tk.Entry(bg, width = 100, textvariable = new_one)
ent_two = tk.Entry(bg, width = 100, textvariable = new_two)
#Do_What
but_y = tk.Button(bg, text = '确定',
                 command = lambda:code(ent_one.get(), ent_two.get()))
but_n = tk.Button(bg, text = '重置', command = no)
but_q = tk.Button(bg, text = '退出', command = qu)
#Where
plan.place(x = 20, y = 10, height = 20)
lab_one.place(x = 20, y = 40, width = 80, height = 20)
lab_two.place(x = 20, y = 80, width = 80, height = 20)
ent_one.place(x = 120, y = 40, width = 80, height = 20)
ent_two.place(x = 120, y = 80, width = 80, height = 20)
but_y.place(x = 170, y = 220, width = 50, height = 20)
but_n.place(x = 100, y = 220, width = 50, height = 20)
but_q.place(x = 30, y = 220, width = 50, height = 20)
#End
bg.mainloop()
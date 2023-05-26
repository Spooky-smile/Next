import random
print('感谢使用本程序，期望它能解决您的困扰。')
mun1 = input('请键入计划一：')
mun2 = input('请键入计划二：')
end = random.randint(1, 2)
if end == 1:
    print('你的计划是', mun1)
else:
    print('你的计划是', mun2)
what = input("Let's to do, just now." )
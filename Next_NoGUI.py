#确认计划数量 > 生成对应的计划项
#确定各计划项内容 > 随机排序
#输出计划列表

#Head
import random
#In
mun =int(input("Your Plans munber is:"))
print("OK, please input your Plans.")
#WorkCode
i = 2
#In
one = input("")
two = input("")
#WorkCode
end = random.randint(1,2)
if end == 1:
    print('Your plan is', one)    
else:
    print('Your plan is', two)

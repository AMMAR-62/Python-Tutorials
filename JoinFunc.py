# l1 = ["John Cena","Randy Orton","Khali","Jindar Mahal","Sheamus"]
# a = " and ".join(l1)
# print(a,"other wwe superstar")
# num = ["3","16","64"]
# num = list(map(int,num))
# num = list(map(lambda x:x*x,num))
# print(num)
# num = [45,4,54,12,147,8,12,1,872,12,47]
# def square(x):
#     return x*x
# def Cube(x):
#     return x**3
# func = [square,Cube]
# val = []
# for i in range(5):
#     val.append(list(map(lambda x:x(i),func)))

# print(val)
# list_1 = [1,2,3,4,5,6,7,8,9]
# def is_greater_5(num):
#     return num>5
# gr_than_5 = list(filter(is_greater_5,list_1))
# print(gr_than_5)

# ////////////////////REDUCE ////////////////
from functools import reduce
list_1 = [1,2,3,4]
# num = 0
# for i in list_1:
#     num = num + i
num =reduce(lambda x,y: x+y,list_1)
print(num)
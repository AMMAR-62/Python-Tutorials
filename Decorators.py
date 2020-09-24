# def function1():
#     print("Subscribe NOw")
# func2 = function1
# del function1
# func2()

# def function1(num):
#     if num==0:
#         return print
#     if  num==1:
#         return int
# a = function1(0)
# print(a)

# def executor(func):
#     func("this")

# executor(print)

# -----------DECORATORS -----------
def deck1(func1):
        print("Executing Now")
        func1()
        print("Executed")
@deck1
def A():
    print("Ammar is Awesome and all are bwelow him")
    return 5+6
A()
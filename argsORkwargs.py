# def Function_name_print(a,b,c,d,e):
#     print(a,b,c,d)
def funargs(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    print("Now i would like to introduce some of are heroes")
    for i,value in kwargs.items():
        print(f"{i} is a {value}")

normal = "The Students are"
har = ["Harry","Rohan","Skillf","Hammad","Shivam"]
kw = {"Rohan":"Monitor","Harry":"Fitness Instructor","Hammad":"Hammi"}
funargs(normal,*har,**kw)
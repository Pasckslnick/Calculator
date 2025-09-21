prov = False
d=["+","-","*","/","//","%","**",">","<",">=","<=","==","!="]

while True:
    try:  
        a=float(input("Пожалуйста введите первое число: "))   
        break
    except:  
        print("Вы ошиблись в вводе первого числа") 

z=str(input("Введите действие: "))
    
while z not in d:
    print("Увы такого действия не может выполнить данный калькулятор.")
    z=str(input("Введите действие: "))   

while True:
    try:  
        b=float(input("Пожалуйста введите второе число: "))   
        break
    except:  
        print("Вы ошиблись в вводе второго числа")




if b == 0:
    prov = prov is not True

if z in d:

    "Действия"
    def sum(a,b):
        print(a+b)
    def sub(a,b):
        print(a-b)
    def mul(a,b):
        print(a*b)
    def div(a,b):
        print(a/b)
    def di(a,b):
        print(a//b)
    def pr(a,b):
        print(a%b)
    def st(a,b):
        print(a**b)

    "Сравненичя"
    def rav(a,b):
        print(a == b)
    def nerav(a,b):
        print(a != b)
    def bol(a,b):
        print(a > b)
   
    def men(a,b):
        print(a < b)
    def bolr(a,b):
        if a>b or b==a:
            c=True
        else:
            c=False
        print(c)
    def menr(a,b):
        if a<b or b==a:
            c=True
        else:
            c=False
        print(c)


    if z=="==":
        rav(a,b)
    elif z=="!=":
        nerav(a,b)
    elif z==">":
        bol(a,b)
    elif z=="<":
        men(a,b)
    elif z==">=":
        bolr(a,b)
    elif z=="<=":
        menr(a,b)



    elif z=="+":
        sum(a,b)
    elif z=="-":
        sub(a,b)
    elif z=="*":
        mul(a,b)
    elif z=="/" and not prov!=False:
        div(a,b)
    elif z=="//" and not prov!=False:
        di(a,b)
    elif z=="%" and not prov!=False:
        pr(a,b)
    elif z=="**":
        st(a,b)
    else:
        print("Возникла непредвиденная ошибка")

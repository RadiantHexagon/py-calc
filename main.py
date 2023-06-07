def com():
        a = input("What is your first number? ")
        a = int(a)
        x = input("What is your second number? ")
        x = int(x)
        if a>x:
            print (str(a) + " is greater than " + str(x))
        if a<x:
            print(str(a) + " is less than " + str(x))
        if a==x:
            print(str(a) + " is equal to " + str(x))
        y = input("Tell me 'again' if you want me to calculate another number! ")
        if y == "again":
            f = input("What operation do you want to do? Add, Sub, Mul, Div, Com, Sqa, Cub, or Pow? ")
        if f == "Add":
            add()
        if f == "Sub":
            sub()
        if f == "Mul":
            mul()
        if f == "Div":
            div()
        if f == "Com":
            com()
        if f == "Sqa":
            sqa()
        if f == "Cub":
            cub()
        if f == "Pow":
            pow()
def add():
        a = input("What is your first number? ")
        a = int(a)
        x = input("What is your second number? ")
        x = int(x)
        print ("The sum of " + str(a) + " and " + str(x) + " is " + str(x+a))

        y = input("Tell me 'again' if you want me to calculate another number! ")
        if y == "again":
            f = input("What operation do you want to do? Add, Sub, Mul, Div, Com, Sqa, Cub, or Pow? ")
        if f == "Add":
            add()
        if f == "Sub":
            sub()
        if f == "Mul":
            mul()
        if f == "Div":
            div()
        if f == "Com":
            com()
        if f == "Sqa":
            sqa()
        if f == "Cub":
            cub()
        if f == "Pow":
            pow()
def sub():
        a = input("What is your first number? ")
        a = int(a)
        x = input("What is your second number? ")
        x = int(x)
        print ("The difference of " + str(a) + " and " + str(x) + " is " + str(a-x))
        y = input("Tell me 'again' if you want me to calculate another number! ")
        if y == "again":
            f = input("What operation do you want to do? Add, Sub, Mul, Div, Com, Sqa, Cub, or Pow? ")
        if f == "Add":
            add()
        if f == "Sub":
            sub()
        if f == "Mul":
            mul()
        if f == "Div":
            div()
        if f == "Com":
            com()
        if f == "Sqa":
            sqa()
        if f == "Cub":
            cub()
        if f == "Pow":
            pow()
f = input("What operation do you want to do? Add, Sub, Mul, Div, Com, Sqa, Cub, or Pow? ")
def mul():
        a = input("What is your first number? ")
        a = int(a)
        x = input("What is your second number? ")
        x = int(x)
        print ("The product of " + str(a) + " and " + str(x) + " is " + str(a*x))

        y = input("Tell me 'again' if you want me to calculate another number! ")
        if y == "again":
            f = input("What operation do you want to do? Add, Sub, Mul, Div, Com, Sqa, Cub, or Pow? ")
        if f == "Add":
            add()
        if f == "Sub":
            sub()
        if f == "Mul":
            mul()
        if f == "Div":
            div()
        if f == "Com":
            com()
        if f == "Sqa":
            sqa()
        if f == "Cub":
            cub()
        if f == "Pow":
            pow()
def div():
        a = input("What is your first number? ")
        a = int(a)
        x = input("What is your second number? ")
        x = int(x)
        print ("The quotient of " + str(a) + " and " + str(x) + " is " + str(a/x))

        y = input("Tell me 'again' if you want me to calculate another number! ")
        if y == "again":
            f = input("What operation do you want to do? Add, Sub, Mul, Div, Com, Sqa, Cub, or Pow? ")
        if f == "Add":
            add()
        if f == "Sub":
            sub()
        if f == "Mul":
            mul()
        if f == "Div":
            div()
        if f == "Com":
            com()
        if f == "Sqa":
            sqa()
        if f == "Cub":
            cub()
        if f == "Pow":
            pow()
def sqa():
        a = input("What is your number? ")
        a = int(a)
        print (str(a) + " squared is equal to " + str(a*a))
        y = input("Tell me 'again' if you want me to calculate another number! ")
        if y == "again":
            f = input("What operation do you want to do? Add, Sub, Mul, Div, Com, Sqa, Cub, or Pow? ")
        if f == "Add":
            add()
        if f == "Sub":
            sub()
        if f == "Mul":
            mul()
        if f == "Div":
            div()
        if f == "Com":
            com()
        if f == "Sqa":
            sqa()
        if f == "Cub":
            cub()
        if f == "Pow":
            pow()
def cub():
        a = input("What is your number? ")
        a = int(a)
        print (str(a) + " cubed is equal to " + str(a*a*a))
        y = input("Tell me 'again' if you want me to calculate another number! ")
        if y == "again":
            f = input("What operation do you want to do? Add, Sub, Mul, Div, Com, Sqa, Cub, or Pow? ")
        if f == "Add":
            add()
        if f == "Sub":
            sub()
        if f == "Mul":
            mul()
        if f == "Div":
            div()
        if f == "Com":
            com()
        if f == "Sqa":
            sqa()
        if f == "Cub":
            cub()
        if f == "Pow":
            pow()
def pow():
        a = input("What is your first number? ")
        a = int(a)
        x = input("What is your second number? ")
        x = int(x)
        print (str(a) + " to the power of " + str(x) + " is equal to " + str(a**x))
        y = input("Tell me 'again' if you want me to calculate another number! ")
        if y == "again":
            f = input("What operation do you want to do? Add, Sub, Mul, Div, Com, Sqa, Cub, or Pow? ")
        if f == "Add":
            add()
        if f == "Sub":
            sub()
        if f == "Mul":
            mul()
        if f == "Div":
            div()
        if f == "Com":
            com()
        if f == "Sqa":
            sqa()
        if f == "Cub":
            cub()
        if f == "Pow":
            pow()
f = input("What operation do you want to do? Add, Sub, Mul, Div, Com, Sqa, Cub, or Pow? ")
if f == "Add":
    add()
if f == "Sub":
    sub()
if f == "Mul":
    mul()
if f == "Div":
    div()
if f == "Com":
    com()
if f == "Sqa":
    sqa()
if f == "Cub":
    cub()
if f == "Pow":
    pow()
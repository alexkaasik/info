#Aleks Kaasik TITpv20
#1
print("1 Максимальное")
o=eval(input("put number"))
while type(o)!=int:  #если не дробное число, повторям вопрос
    try:
        a=int(input("o"))
    except:
        TypeError
max_=int(input("1 - number:"))
for o in range(2,o+1):
    arv=int(input(f"put {o} number"))
    if arv>max_:
        max_=arv
print(f"the biggest number:{max_} ")
        
#2
print("2 Кроме13")
N=eval(input("put number"))

while type(N)!=int:
    try:
        N=int(input("put number"))
    except:
          ValueError
if N==13:
    print("77")
else:
    print(N)


#3
print("3 Пробежал")
d1=10
summa=10
print(f"first day{d1}\n{summa}")
for i in range(2,8):
    d1*=1.1
    summa+=d1
    print (f"{i}day{d1}\n{summa}")

#4
print("4 Ткани")
M=100

n=int(input("how much"))
if n<=M:
    M-=n
    print(f"\ngood")
else:
    print("no can't")


#5
print("5 Трапеции")
a = int(input("put a"))
b = int(input("put b"))
h = int(input("put h"))

A=(a+b)/2*h
print(A)


#6
print("6 Без остатка на 3.")
x=int(input("a number"))
if x%3==0:
    print("yes")
else:
    print("no")

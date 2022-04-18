#3.	Вывести на экран числа от -N до N
import os
os.system ("cls")
a = int(input("Введитте число - "))
f=set(range(-a,a))
print(f)
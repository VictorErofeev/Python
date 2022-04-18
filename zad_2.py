#2.	Найти максимальное из пяти чисел
import os
os.system ("cls")
masiv = [1,72,25,4,83]
max=0
for i in masiv:
    if i>max:
        max=i

print('Максимальное число - ', max)
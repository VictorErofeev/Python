#9.	Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
import os
os.system ("cls")
a = int(input("Введитте четверти прямоугольной системы координат - "))
if a>4:print("Данной четверти нет в прямоугольной системе координат")
if a<0:print("Отрицательной четверти нет в прямоугольной системе координат")
if a==0:print("Нет такой четверти, введитте четверть прямоугольной системы координат от 1 до 4")
if a==1:print('Допустимые значения координат точки (X>0 до ∞; Y>0 до ∞)')
if a==2:print('Допустимые значения координат точки (X<0 до -∞; Y>0 до ∞)')
if a==3:print('Допустимые значения координат точки (X<0 до -∞; Y<0 до -∞)')
if a==4:print('Допустимые значения координат точки (X>0 до ∞; Y<0 до -∞)')
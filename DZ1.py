import math #подключение библиотеки

def resh(): #создаем функцию
    a = float(input("a = ")) #ввод переменных, присвоение им значений
    b = float(input("b = "))
    c = float(input("c = "))

    if a + b >c and a + c > b and b + c > a: #проверка существования треугольника
        print ("треугольник существует")
        return (a,b,c)
    else: 
        print ("треугольник не существует")
    j = resh() 
    return(j)


a,b,c = resh()

p = (a + b + c)/2 #нахождение полупериметра
print("p = ", p)

r = math.sqrt(((p - a) * (p-b) * (p-c)) / p) #нахождение радиуса
print("r = ", r)

S = math.pi * r **2 #нахождение площади
print("S = ", S)

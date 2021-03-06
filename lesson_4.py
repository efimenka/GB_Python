#1
from sys import argv
name, a, b, c = argv
print("Заработная плата = ", (int(a)*int(b)) + int(c))

#2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
#Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#Результат: [12, 44, 4, 10, 78, 123].

z = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
z_new = [n for i, n in enumerate(z) if i > 0 and z[i] > z[i-1]]
print(z_new)

#3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#Подсказка: использовать функцию range() и генератор.

z_new = [n for n in range(20,240) if n%20==0 or n%21==0]
print(z_new)

#4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
#Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#Результат: [23, 1, 3, 10, 4, 11]

z =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
z_new = [n for n in z if z.count(n) < 2]
print(z_new)

#5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().
from functools import reduce


def my_func(a, b):
    return a*b

print(reduce(my_func, [n for n in range(99,1001) if n%2==0]))


#6. Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

c = 0
for i in cycle("sda"):
    if c > 10:
        break
    print(i)
    c += 1
#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from itertools import count
from math import factorial

def fact():
    for n in count(1):
        yield factorial(n)

gen = fact()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break
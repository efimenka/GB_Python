#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.***

a = int(1)
b = float(2)
c = complex(3, 2)
d = "строка"
e = list(d)
f = tuple(e)
g = set(e)
h = dict(key_1='odin', key_2='dva')
i = False
j = b'text'
k = None

spisok = (a, b, c, d, e, f, g, h, i, j, k)
for i in spisok:
    print(type(i))

#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
lst = []

n = int(input("Введите количнество элементов списка:"))

# заполнение
for i in range(0, n):
    k = int(input("Введите элемент: "))
    lst.append(k)

print(lst)

j = 0
for i in range(int(len(lst) / 2)):
    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    j += 2

print(lst)
#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month = int(input("Введите месяц:"))

year = dict(zima=(12, 1, 2), vesna=(3, 4, 5), leto=(6, 7, 8), osen=(9,10,11))

for k in year.keys():
    if month in year[k]:
        print(k)

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
stroka = input("Введите строку:")
m = stroka.split()
n = len(m)
new = []
for i in range(0,n):
    if len(m[i])>=10:
        new.append(m[i][0:10])
    else:
        new.append(m[i])
for i in enumerate(new):
    print(i)

#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

a = int(input("Введите число:"))
spisok = [7, 5, 3, 3, 2]
max_value = max(spisok)
if a > max_value:
    spisok.insert(0,a)
elif a in spisok:
    print(spisok.index(a))
    spisok.insert(spisok.index(a), a)
else:
    spisok.append(a)
print(spisok)

#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#Пример готовой структуры:
#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]
#Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
#Пример:
#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}

tovar = []
while input("Введите товар (да/нет): ") == 'да':
    nomer = int(input("Введите номер товара: "))
    kharak = {}
    while input("Введите характеристику товара (да/нет): ") == 'да':
        kharak_key = input("Ввелите характеристику: ")
        kharak_value = input("Введите значение характеритики: ")
        kharak[kharak_key] = kharak_value
        tovar.append(tuple([nomer, kharak]))
print(tovar)
analitika = {}
for t in tovar:
    for kharak_key, kharak_value in t[1].items():
        if kharak_key in analitika:
            analitika[kharak_key].append(kharak_value)
        else:
            analitika[kharak_key] = [kharak_value]
print(analitika)

goods = []
while input("Would you like add product? Enter yes/no: ") == 'yes':
    number = int(input("Enter product number: "))
    features = {}
    while input("Would you like add product parameters? Enter yes/no: ") == 'yes':
        feature_key = input("Enter feature product: ")
        feature_value = input("Enter feature value product: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
#goods = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)
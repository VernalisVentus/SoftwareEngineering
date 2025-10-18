Отчет по Теме #6 выполнила:
- Мансурова Елена Ильгизовна
- ПИЭ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |


знак "+" - задание выполнено; знак "-" - задание не выполнено;

---
# Лабораторная работа 6

##ТЕМА 6. Базовые коллекции: словари, кортежи##

---

---

## Задание 1
В школе, где вы учились, узнали, что вы крутой программист и
попросили написать программу для учителей, которая будет при вводе
кабинета писать для него ключ доступа и статус, занят кабинет или нет.
При написании программы необходимо использовать словарь (dict),
который на вход получает номер кабинета, а выводит необходимую
информацию. Если кабинета, который вы ввели нет B словаре, то B
консоль B виде значения ключа нужно вывести “№опе” и виде статуса
вывести “False”. 


```python
request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False},
}

response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_6/pics6/Рисунок1.png)

**Вывод:** с помощью словарей удобно обращаться к элементу по ключу. С помощью такой конструкции мы заменяем конструкцию `if/elif/else`.

---

## Задание 2
Алексей решил создать самый большой словарь B мире. Для этого он
придумал функцию dict maker (**kwargs), которая принимает
неограниченное количество параметров «ключ: значение» и обновляет
созданный UM словарь my_dict, состоящий всего U3 одного элемента
«firsty со значением «50 easy». Помогите Алексею создать данную
функцию. 


```python
from pprint import pprint
my_dict = {'first':'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1=1, a2=20, a3=54, a4= 13)
dict_maker(name='Елена', age=20, weight=55, eyes_color='green')
pprint(my_dict)
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_6/pics6/Рисунок2.png)

**Вывод:** с помощью функций и `**kwargs` можно динамически создавать словари. `pprint` позволяет удобно вывести инормацию.

---

## Задание 3
Для решения некоторых задач бывает необходимо разложить строку на
отдельные символы. Мы знаем что это можно сделать при помощи
split(), у которого более гибкая настройка для разделения для этого, но
если нам нужно посимвольно разделить строку без всяких условий, то
для этого мы можем использовать кортежи (tuple). Для этого напишем
любую строку, которую будем делить и “обвернем” ее B tuple и дальше
мы можем как нам угодно с ней работать, например, сделать ее
списком (тогда получится полный аналог split()) или же работать ¢ ним
дальше, как с кортежем.


```python
input_string = 'HelloWorld'
result=tuple(input_string)
print(result)
print(list(result))
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_6/pics6/Рисунок3.png)

**Вывод:** с помощью `tuple` можно посимвольно разделить строку без всяких условий.

---

## Задание 4
Вовочка решил написать крутую функцию, которая будет писать имя,
возраст и место работы, HO при этом на вход этой функции будет
поступать кортеж. Помогите Вовочке написать эту программу. 


```python
def personal_info(name, age, company='unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

tom = ("Григорий", 22)
personal_info(*tom)

bob = ("Георгий", 41, "Yandex")
personal_info(*bob)
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_6/pics6/Рисунок4.png)

**Вывод:** на вход функции в качестве аргументов можно выставить кортеж.

---

## Задание 5
Для сопровождения первых лиц государства X нужен кортеж, но никто
не может определиться с порядком машин, поэтому вам нужно
написать функцию, которая будет сортировать кортеж, состоящий из
целых чисел по возрастанию, и возвращает его. Если хотя бы одиНн
элемент не является целым числом, TO фуНКЦИЯ возвращает ИСХОДНЬ[Й
кортеж.


```python
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((5,5,3,1,9)))
    print(tuple_sort((5,5,2.1,'1',9)))
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_6/pics6/Рисунок5.png)

**Вывод:** кортеж можно также сортировать и проверять каждый элемент в нём.

---

# Самостоятельная работа

---

## Задание 1

принять от пользователя последовательность чисел, разделённых запятыми, затем вернуть эти данные в виде списка и кортежа.

```python

def parse_numbers_to_list_and_tuple(s):
    parts = s.split(',')
    lst = []
    for i in range(len(parts)):
        token = parts[i].strip()
        if token == '':
            continue
        try:
            num = int(token)
        except ValueError:
            continue
        lst.append(num)
    tpl = tuple(lst)
    return lst, tpl
if __name__ == '__main__':
    s = "1, 2, 3, 4, 5"
    my_list, my_tuple = parse_numbers_to_list_and_tuple(s)
    print("Исходная строка:", s)
    print("Список:", my_list)
    print("Кортеж:", my_tuple)

```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_6/pics6/Рисунок6.png)

**Вывод: **Простая и надёжная функция — вручную разбивает строку, приводит к целым и возвращает список и кортеж. Устойчиво к пробелам и пустым токенам.

---

## Задание 2

написать функцию, которая удаляет первое появление заданного значения из кортежа и возвращает новый кортеж. Если такого элемента нет — вернуть исходный кортеж (без изменений).

```
def remove_first_from_tuple(tpl, value):
    found_index = -1
    for i in range(len(tpl)):
        if tpl[i] == value:
            found_index = i
            break
    
    if found_index == -1:
        return tpl
    
    new_list = []
    for i in range(len(tpl)):
        if i != found_index:
            new_list.append(tpl[i])
    
    return tuple(new_list)

if __name__ == '__main__':
    examples = [
        ((1, 2, 3), 1),
        ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
        ((2, 4, 6, 6, 4, 2), 9)
    ]

    for tpl, val in examples:
        print("Исходный кортеж:", tpl, "Удалить:", val)
        res = remove_first_from_tuple(tpl, val)
        print("Результат:", res)
        
```
![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_6/pics6/Рисунок7.png)
---
**Вывод: **Функция корректно удаляет первое найденное вхождение (при этом кортежы остаются неизменяемыми - мы создаём новый). Если элемент отсутствует, возвращаем исходный кортеж.

---

## Задание 3

дана строка, содержащая символы '0'..'9' (длина ≥ 15). Нужно создать словарь, где ключ — цифра (тип int), значение — количество её вхождений в строке. Затем *из этого словаря* функция должна вернуть словарь из 3-х самых часто встречающихся чисел (ключи — int, значения — количества). Результат вывести в порядке возрастания ключа.


```
def top_three_counts(s):
    count_dict = {}
    for char in s:
        digit = int(char)
        count_dict[digit] = count_dict.get(digit, 0) + 1
    
    print("Полный словарь:", dict(sorted(count_dict.items())))
    
    sorted_items = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    top_three = dict(sorted_items[:3])
    
    result = dict(sorted(top_three.items()))
    print("Топ-3:", result)
    return result

s = "123456789012345678901234"
top_three_counts(s)
```
![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_6/pics6/Рисунок8.png)
---

**Выводы:**
* Для выбора трёх самых частых элементов реализован алгоритм выбрать максимум 3 раза
* Итоговый словарь возвращает ровно 3 пары {digit: count} (если в исходном тексте меньше трёх разных цифр - возвращает столько, сколько есть), и при выводе ключи упорядочены по возрастанию.

---

## Задание 4

Условие: Написать функцию, которая принимает кортеж и случайный элемент (значение) x. Нужно вернуть новый кортеж, начинающийся с первого появления x и заканчивающийся вторым появлением x (включительно).

```
from typing import Tuple, Any

def slice_first_to_second(tpl: Tuple[Any, ...], x: Any) -> Tuple[Any, ...]:
    try:
        first = tpl.index(x)
    except ValueError:
        return ()
    try:
        second = tpl.index(x, first+1)
    except ValueError:
        return tpl[first:]
    return tpl[first:second+1]

if __name__ == '__main__':
    print(slice_first_to_second((1,2,3), 8))          
    print(slice_first_to_second((1,8,3,4,8,9,2), 8))      
    print(slice_first_to_second((1,2,8,5,1,2,9), 8))             
```
![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_6/pics6/Рисунок9.png)
**Вывод: **Функция корректно обрабатывает все три случая (0, 1 и ≥2 вхождений)

---

## Задание 5

Дан список целых чисел. Нужно вернуть кортеж из тех элементов, которые встречаются ровно два раза в исходном списке. Порядок элементов в результате - в порядке первого появления каждого такого числа в исходном списке. Если таких элементов нет - вернуть пустой кортеж.

```
from collections import Counter
from typing import List,Tuple

def elements_with_count_two(lst: List[int]) -> Tuple[int, ...]:
    counts=Counter(lst)
    seen=set()
    result=[]
    for x in lst:
        if counts[x]==2 and x not in seen:
            result.append(x)
            seen.add(x)
    return tuple(result)

if __name__=='__main__':
    print(elements_with_count_two([1,2,3,2,4,1,5])) 
    print(elements_with_count_two([7,7,7,7]))      
    print(elements_with_count_two([9,8,9,8,7,7]))   
```
![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_6/pics6/Рисунок10.png)
**Вывод: ** Задача проверяет логику подсчёта и сохранения порядка первого появления. 

---
# Общий вывод

Коллекции данных (списки, кортежи, множества, словари) - основа хранения и обработки информации в Python.
* Списки (list) - изменяемые упорядоченные коллекции, удобные для добавления и удаления элементов.
* Корежи (tuple) - неизменяемые последовательности, часто применяются для хранения фиксированных данных.
* Множества (set) - неупорядоченные коллекции уникальных элементов, полезные при фильтрации повторов.
* Словари (dict) - хранят пары ключ - значение и обеспечивают быстрый доступ к данным по ключу.

Использование встроенных структур данных, таких как Counter, set, а также понимание принципов итерации и индексации позволяют создавать эффективные алгоритмы для анализа и обработки информации.






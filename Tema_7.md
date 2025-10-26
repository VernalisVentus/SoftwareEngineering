Отчет по Теме #7 выполнила:
- Мансурова Елена Ильгизовна
- ПИЭ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |  |
| Задание 7 | + |  |
| Задание 8 | + |  |
| Задание 9 | + |  |
| Задание 10 | + |  |


знак "+" - задание выполнено; знак "-" - задание не выполнено;

---
# Лабораторная работа 7

#ТЕМА 7. Работа с файлами (ввод, вывод)

---

## Задание 1
Составьте текстовый файл и положите его в одну директорию с
программой на Руфоп. Текстовый файл должен состоять минимум из
двух строк. 


```python
Hello students!
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок1.png)

**Вывод:** файл должен находиться в директории, где находится файл с кодом.

---

## Задание 2
Напишите программу, которая выведет только первую строку из
вашего файла, при этом используйте конструкцию open()/close(). 


```python
f = open('input.txt','r')
print(f.readline())
f.close()
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок2.png)

**Вывод:** с помощью readline() можно считать строку из файла. `open` позволяет ввест путь к файлу и модификатор доступа - в данном случае `r`.

---

## Задание 3
Напишите программу, которая выведет все строки из вашего файла B
массиве, при этом используйте конструкцию open()/close().


```python
f = open('input.txt','r')
print(f.readlines())
f.close()
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок3.png)

**Вывод:** с помощью readlines() можно считать строки массивом из файла.

---

## Задание 4
Напишите программу, которая выведет все строки из вашего файла B
массиве, при этом используйте конструкцию with ореп(). 

```python
with open('input.txt') as f:
    print(f.readlines())
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок4.png)

**Вывод:** with open предоставляет удобство в последующем использовании файла в программе.

---

## Задание 5
Напишите программу, которая выведет каждую CTPOKY U3 вашего
файла отдельно, при этом используйте конструкцию with open(). 


```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок5.png)

**Вывод:** каждую строку можно вывести отдельно с помощью цикла.

---

## Задание 6
Напишите программу, которая будет добавлять новую строку B ваш
файл, а потом выведет полученный файл в консоль. Вывод можно
осуществлять любым способом. Обязательно проверьте сам файл,
чтобы изменения в нем тоже отображались. 

```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок6.png)

**Вывод:** различные модификаторы доступа к файлу предоставляют различные возможности в работе с ним, так например `a+` позволяет добавить строку в файл.

---

## Задание 7
Напишите программу, которая перепишет всю информацию, которая
была у вас в файле до этого, например напишет любые данные из
произвольно вами составленного списка. Также не забудьте проверить
что измененная вами информация сохранилась в файле.

```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок7.png)

**Вывод:** с помощью цикла таким способом можно записать сразу много строк в файл.

---

## Задание 8
Выберите любую папку на своем компьютере, имеющую вложенные
директории. Выведите на печать в терминал ее содержимое, как и всех
подкаталогов при помощи функции print_docs(directory). 


```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)

print_docs('E:/Documents/SoftwareEngineering/theme_7/theme_7')
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок8.png)

**Вывод:** `os` позволяет работать с функциями операционной и файловой системы. 

---

## Задание 9
Документ «input.txt» содержит следующий текст:
Приветствие
Спасибо
Извините
Пожалуйста
До свидания
Ты готов?
Как дела?
С днем рождения!
Удача!
Я тебя люблю.
Требуется реализовать функцию, которая выводит слово, имеющее
максимальную длину (или список слов, если таковых несколько).
Проверьте работоспособность программы на своем наборе данных


```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок9.png)

**Вывод:** можно также обрабатывать строки из файла и искать среди них максимальную длину слова.

---

## Задание 10
Требуется создать сзу-файл «rows_300.csv» со следующими
столбцами:
® Ne - номер по порядку (от 1 до 300);
® CexyHJa — текущая секунда на вашем ПК;
® — Микросекунда — текущая миллисекунда на часах.
Для наглядности на каждой итерации цикла искусственно
приостанавливайте скрипт на 0,01 секунды. 

```python
import csv
import datetime
import time

with open('rown_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
    time.sleep(0.01)

```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок10.png)

**Вывод:** м помощью функций открытия файлов можно также открывать табличные csv файлы и вставлять в них данные.

---

# Самостоятельная работа №7

---

## Задание 1

**Формулировка:**
Найти в интернете статью (≥200 слов), сохранить её в файл и написать программу,
которая подсчитывает количество слов и находит самое часто встречающееся слово.

```python
from collections import Counter

with open("article.txt", encoding="utf-8") as f:
    text = f.read().lower().split()

word_count = len(text)
most_common = Counter(text).most_common(1)[0]

print(f"Количество слов: {word_count}")
print(f"Самое частое слово: '{most_common[0]}' — встречается {most_common[1]} раз(а)")
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок11.png)

**Вывод:**
Программа корректно подсчитала общее количество слов в файле и определила слово, встречающееся чаще всего.

---

## Задание 2

Создать программу для ведения книги расходов: ввод данных через консоль,
запись в файл и вывод всех записей.

```python
def add_expense(filename):
    category = input("Категория: ")
    amount = float(input("Сумма: "))
    note = input("Комментарий: ")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{category},{amount},{note}\n")

def show_expenses(filename):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            category, amount, note = line.strip().split(",")
            print(f"{category}: {amount} руб. - {note}")

if __name__ == "__main__":
    add_expense("expenses.txt")
    print("\nТекущие расходы:")
    show_expenses("expenses.txt")
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок12.png)

**Вывод:**
Программа позволяет добавлять новые расходы и просматривать список всех трат из файла, корректно записывая и читая данные.

---

## Задание 3

Прочитать текст из `input.txt` и вывести количество букв латинского алфавита, слов и строк.

```python
with open("input.txt", encoding="utf-8") as f:
    lines = f.readlines()

text = "".join(lines)
letters = sum(ch.isalpha() for ch in text)
words = len(text.split())
lines_count = len(lines)

print("Содержимое файла:")
print(f"Букв: {letters}")
print(f"Слов: {words}")
print(f"Строк: {lines_count}")
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок13.png)

**Вывод:**
Программа успешно подсчитала статистику по текстовому файлу, определив количество букв, слов и строк.

---

## Задание 4

Написать программу, которая заменяет все запрещённые слова в предложении на звёздочки `*`.
Запрещённые слова хранятся в `input.txt` и заменяются независимо от регистра.

```python
import re

with open("input.txt", "r", encoding="utf-8") as f:
    banned_words = [line.strip() for line in f if line.strip()]

sentence = "Это плохое и запрещенное СЛОВО не стоит использовать"

pattern = r'\b(' + '|'.join(re.escape(word) for word in banned_words) + r')\b'
result = re.sub(pattern, lambda m: '*' * len(m.group()), sentence, flags=re.IGNORECASE)

print("Результат:")
print(result)
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок14.png)

**Вывод:**
Все запрещённые слова заменяются звёздочками с сохранением длины слова и без учёта регистра.

---

## Задание 5

Придумать и реализовать собственную задачу с взаимодействием с файлом.
**Пример:** программа, которая создаёт файл `quotes.txt` и выводит случайную цитату.

```python
import random

movies = [
    "Форсаж",
    "Мстители",
    "Пираты Карибского моря",
    "Гарри Поттер",
    "Властелин колец",
    "Матрица",
    "Назад в будущее",
    "Терминатор",
    "Чужой",
    "Хищник"
]

with open("quotes.txt", "w", encoding="utf-8") as f:
    for movie in movies:
        f.write(movie + "\n")

with open("quotes.txt", "r", encoding="utf-8") as f:
    all_movies = f.readlines()
    random_movie = random.choice(all_movies).strip()

print("Случайный фильм для просмотра:")
print(random_movie)
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_7/pics7/Рисунок15.png)

**Вывод:**
Программа случайным образом выбирает и выводит цитату из текстового файла, демонстрируя чтение и выбор данных из файла.

---

## Общий вывод по теме 7

Работа с файлами - один из базовых навыков Python-разработчика.

* **Открытие и чтение (`open`, `read`, `readlines`)** позволяет получать данные из вн источников.
* **Запись (`write`, `writelines`, режим `a`)** используется для сохранения инф-ии.
* **Контекстный менеджер (`with open(...)`)**  автоматическое закрытие файла.

Изучение этой темы позволяет создавать полноценные программы, которые читают, анализируют и сохраняют данные.


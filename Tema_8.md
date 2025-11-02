Отчет по Теме 8 выполнила:
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
# Лабораторная работа 8

# ТЕМА 8. Введение в ООП

---

## Задание 1
Создайте класс “Саг” с атрибутами производитель и модель. Создайте
объект этого класса. Напишите комментарии для кода, объясняющие
его работу. Результатом выполнения задания будет листинг кода с
комментариями. 


```python
class Car:
    def __init__(self, make, model): #функция инициализации 
        self.make = make #марка
        self.model = model #модель

my_car = Car("Toyota", "Corolla") #создание объекта
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_8/pics8/Рисунок1.png)

**Вывод:** с помощью `class` можно создать класс и инициализироват его.

---

## Задание 2
Дополните код U3 первого задания, добавив B него атрибуты и методы
класса, заставьте машину “поехать”. Напишите комментарии для кода,
объясняющие его работу. Результатом выполнения задания будет
листинг кода с комментариями и получившийся вывод в консоль. 


```python
class Car:
    def __init__(self, make, model): #функция инициализации 
        self.make = make #марка
        self.model = model #модель
    
    def drive(self):
        print(f"Едем на {self.make} {self.model}")

my_car = Car("Toyota", "Corolla") #создание объекта
my_car.drive()
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_8/pics8/Рисунок2.png)

**Вывод:** внутри класса можно добавлять атрибуты и методы класса.

---

## Задание 3
Создайте новый класс “ElectricCar” с методом “charge” и атрибутом
емкость батареи. Реализуйте ero наследование от класса, созданного B
первом задании. Заставьте машину поехать, а потом заряжаться.
Напишите комментарии для кода, объясняющие его работу.
Результатом выполнения задания будет листинг кода с комментариями
и получившийся вывод в консоль. 


```python
class Car:
    def __init__(self, make, model): #функция инициализации 
        self.make = make #марка
        self.model = model #модель
    
    def drive(self):
        print(f"едем на {self.make} {self.model}")

my_car = Car("Toyota", "Corolla") #создание объекта
my_car.drive()

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        print(f"заряжаем {self.make} {self.model} используя {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_8/pics8/Рисунок3.png)

**Вывод:** классы можно наследовать с помощью `class Class1(наследуемый класс)`.

---

## Задание 4
Реализуйте инкапсуляцию для класса, созданного B первом задании.
Создайте защищенный атрибут производителя и приватный атрибут
модели. Вызовите защищенный атрибут и заставьте машину поехать.
Напишите комментарии для кода, объясняющие его работу.
Результатом выполнения задания будет листинг кода с комментариями
и получившийся вывод в консоль. 

```python
class Car:
    def __init__(self, make, model): #функция инициализации 
        self._make = make #марка
        self.__model = model #модель
    
    def drive(self):
        print(f"едем на {self._make} {self.__model}")  
my_car = Car("Toyota", "Corolla") #создание объекта
print(my_car._make)
my_car.drive()

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        print(f"заряжаем {self._make} {self._Car__model}  используя {self.battery_capacity} kWh")  
my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_8/pics8/Рисунок4.png)

**Вывод:** инкапсуляция с помощью `_` или `__` указывает уровень доступа к атрибуту.

---

## Задание 5
Реализуйте полиморфизм создав основной (общий) класс “Shape”, а
также еще два класса “Rectangle” и “Circle”. Внутри последних двух
классов реализуйте методы для подсчета площади фигуры. После этого
создайте массив с фигурами, поместите туда круг и прямоугольник,
затем при помощи цикла выведите их площади. Напишите
комментарии для кода, объясняющие его работу. Результатом
выполнения задания будет листинг кода с комментариями и
получившийся вывод в консоль. 


```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rect = Rectangle(4, 10)
circle = Circle(5)

shapes = [rect, circle]

for shape in shapes:
    print("Площадь фигуры:", shape.area())

```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_8/pics8/Рисунок5.png)

**Вывод:** каждую строку можно вывести отдельно с помощью цикла.

---

# Самостоятельная работа 8

---

## Задание 1
Самостоятельно создать класс и его объект. Класс и объект должны отличаться от примеров из методички.

```python
class MusicTrack:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"Сейчас играет: {self.title} - {self.artist} ({self.duration} сек.)")

track1 = MusicTrack("123", "gaga", 333)

track1.play()
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_8/pics8/Рисунок6.png)

**Вывод:** Создан класс `MusicTrack` с полями для названия, исполнителя и длительности, а также методом `play()`, который выводит информацию о треке.

---

## Задание 2

Добавить собственные атрибуты и методы в ранее созданный класс.

```python
class MusicTrack:
    def __init__(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre

    def play(self):
        print(f"Сейчас играет: {self.title} - {self.artist} ({self.duration} сек.)")

    def info(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        print(f"Продолжительность: {minutes} мин {seconds} сек")

track1 = MusicTrack("123", "gaga", 333, "Electronic")

track1.play()
track1.info()
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_8/pics8/Рисунок7.png)

**Вывод:** Добавлены новые атрибут (`genre`) и метод (`info`), который преобразует длительность трека в минуты и секунды.

---

## Задание 3

Реализовать наследование, продолжая работать с ранее созданным классом.

```python
class MusicTrack:
    def __init__(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre

    def play(self):
        print(f"Сейчас играет: {self.title} - {self.artist} ({self.duration} сек.)")

    def info(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        print(f"Продолжительность: {minutes} мин {seconds} сек")

class Remix(MusicTrack):
    def __init__(self, title, artist, duration, genre, remixer):
        super().__init__(title, artist, duration, genre)
        self.remixer = remixer

    def play(self):
        print(f"{self.title} (Remix by {self.remixer}) - {self.artist} [{self.genre}]")

track1 = MusicTrack("123", "gaga", 333, "Electronic")
track1.play()
track1.info()

remix = Remix("123", "gaga", 333, "Electronic", "DJ")
remix.play()
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_8/pics8/Рисунок8.png)

**Вывод:** Реализовано наследование класса `Remix` от `MusicTrack` с переопределением метода `play()`.

---

## Задание 4

Реализовать инкапсуляцию на основе ранее созданного класса.

```python
class MusicTrack:
    def __init__(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre

    def play(self):
        print(f"Сейчас играет: {self.title} - {self.artist} ({self.duration} сек.)")

    def info(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        print(f"Продолжительность: {minutes} мин {seconds} сек")

    def set_duration(self, seconds):
        if seconds > 0:
            self.__duration = seconds
        else:
            print("Ошибка")

    def get_duration(self):
        return self.__duration

class Remix(MusicTrack):
    def __init__(self, title, artist, duration, genre, remixer):
        super().__init__(title, artist, duration, genre)
        self.remixer = remixer

    def play(self):
        print(f"{self.title} (Remix by {self.remixer}) - {self.artist} [{self.genre}]")

track1 = MusicTrack("123", "gaga", 333, "Electronic")
track1.play()
track1.info()
track1.set_duration(100)
print("Новая длительность трека: ", track1.get_duration())

remix = Remix("123", "gaga", 333, "Electronic", "DJ")
remix.play()
```

**Результат выполнения:**

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_8/pics8/Рисунок9.png)

**Вывод:** Использованы приватные атрибуты (`__title`, `__artist` и др.) и методы доступа (`get_`, `set_`), реализуя инкапсуляцию данных.

---

## Задание 5

**Формулировка:**
Реализовать полиморфизм. Использовать разные классы с одинаковым методом.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Площадь: {shape.area()}")
```

![Результат](https://github.com/VernalisVentus/SoftwareEngineering/blob/theme_8/pics8/Рисунок10.png)


**Вывод:** Реализован полиморфизм.

## Вывод

Объектно-ориентированное программирование представляет собой фундаментальный метод проектирования программных систем, основанный на моделировании реальных объектов и их взаимодействий.
Применение принципов инкапсуляции, наследования, полиморфизма и абстракции позволяет создавать код, который отличается чёткой структурой и улучшенной читаемостью.
Таким образом, выполнение всех заданий помогло глубже понять и применить на практике ключевые концепции ООП в языке Python.



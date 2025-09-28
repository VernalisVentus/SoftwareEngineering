numbers = [1, 52, 4, 6, 8, 10]
value = int(input("Введите число: "))

if value in numbers:
    if value % 2 == 0:
        print("Число четное и находится в массиве")
    else:
        print("Число нечетное и находится в массиве")
else:
    print("Числа нет в массиве")

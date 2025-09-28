x = int(input("Введите число: "))

if x < 0:
    print("Меньше 0")
elif 0 < x < 10:
    print("Больше 0 и меньше 10")
elif x > 10:
    print("Больше 10")
else:
    print("Равно 0")

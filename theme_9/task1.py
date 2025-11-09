class Elena:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Елена':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Елена"

person1 = Elena('Алексей')
person2 = Elena('Елена')
print(person1.name)
print(person2.name)

person2.surname = 'Петрова'
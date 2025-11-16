class NameTooLongException(Exception):
    pass

def check_name(name):
    if len(name) > 10:
        raise NameTooLongException("Длина более 10 символов")
    else:
        print('Успешная регистрация')

if __name__ == '__main__':
    name = '12345678910'
    try:
        check_name(name)
    except NameTooLongException as e:
        print(f"Ошибка: {e}")
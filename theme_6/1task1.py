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

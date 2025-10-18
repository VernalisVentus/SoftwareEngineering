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
        
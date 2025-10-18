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
def filter_list(lst):
    result = []
    for element in lst:
        if isinstance(element, int) and element >= 0:
            result.append(element)

    return result

lst = [1, "a", -2, 5, "hello", 0]
print(filter_list(lst))
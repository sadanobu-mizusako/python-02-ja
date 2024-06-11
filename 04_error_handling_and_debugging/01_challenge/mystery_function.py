def mystery_function(lst):
    result = lst
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            result[i] = lst[i] ** 2
    return result

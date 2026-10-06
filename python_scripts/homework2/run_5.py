def max_min(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

# print(max_min([1, 1, 1, 1, 1]))
# print(max_min([-10, 0, 5, 0, 2]))
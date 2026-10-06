def even_odd(numbers):
    if not numbers:
        return 0, 0
    sum_of_odd = 0
    sum_of_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_of_even += num
        else:
            sum_of_odd += num
    return sum_of_even, sum_of_odd

# print(even_odd([1, 2, 3, 4, 5]))
# print(even_odd([10, 20, 30, 40, 50]))
# print(even_odd([-1, -2, -3, -4, -5]))
# print(even_odd([]))
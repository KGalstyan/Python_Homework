def arhimetic_average(numbers):
    if not numbers:
        return 0
    else:
        return sum(numbers) / len(numbers)

# print(arhimetic_average([1, 2, 3, 4, 5]))
# print(arhimetic_average([0 , 0, 0, 0, 0]))
# print(arhimetic_average([]))
# print(arhimetic_average([1, 2]))
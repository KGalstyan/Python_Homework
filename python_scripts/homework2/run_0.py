def sum_digit(num):
    if num < 10:
        return num
    else:
        return num % 10 + sum_digit(num // 10)

# print(sum_digit(12345))
# print(sum_digit(987654321))
# print(sum_digit(0))
# print(sum_digit(5))
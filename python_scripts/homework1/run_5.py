s = input("Enter a string: ")

count = 0

for char in s:
    if char.lower() in "aeiou":
        count += 1

print(count)
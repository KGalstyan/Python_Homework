items = input("Enter elements: ").split()

unique = []

for item in items:
    if item not in unique:
        unique.append(item)

print(unique)

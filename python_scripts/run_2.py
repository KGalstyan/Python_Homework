s = input("Enter a string: ")

str = ""
for ch in s:
    if ch.isalnum():
        str += ch.lower()

if (str == str[::-1]):
    print(True)
else:
    print(False)
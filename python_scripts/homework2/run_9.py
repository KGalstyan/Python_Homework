def longest_word(sentence):
    words = sentence.split()
    largestword = ""
    for word in words:
        if len(word) > len(largestword):
            largestword = word
    return largestword

# print(longest_word(input()))
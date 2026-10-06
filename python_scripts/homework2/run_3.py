def word_count(words):
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

# print(word_count(["", "", "", "", "", ""]))
# print(word_count([]))
# print(word_count(["hello", "world", "hello"]))
# print(word_count(["aaa", "bbb", "aaa", "ccc", "bcb", "ccc", "aaa"]))
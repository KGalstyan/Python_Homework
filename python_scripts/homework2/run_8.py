def common_list (list1, list2):
    return list(set(list1) & set(list2))

# print(common_list([], []))
# print(common_list([1, 2, 2, 3], [1, 2, 3, 3, 2, 4]))
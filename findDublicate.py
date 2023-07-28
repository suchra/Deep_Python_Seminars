def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

lst = [1,1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 7, 7]
print(find_duplicates(lst))
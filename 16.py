dictt = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
print(type(dictt))
count = {}
for dict in dictt:
    count[dict] = count.get(dict, 0) + 1
print(count)


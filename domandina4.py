list = ["mario", "luigi", "giovanni", "alice"]
list2 = []

for i in list:
    list2.append(i[0].upper() + i[1:])

print(list2)
# Linear Sorting algo

items = [5, 4, 6, 7, 3, 1];
print(items);
l = len(items);
print(l);

for i in range(0, l-1):
    for j in range(i, l):
        if items[i] > items[j] :
            items[i], items[j] = items[j], items[i];
print(items);


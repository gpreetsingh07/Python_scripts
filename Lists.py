even = [10, 2, 4, 6, 8]
odd = [1, 3, 5, 7]

print(even);
even.sort()
print(even);
even.sort(reverse=True)
print(even);

if even == odd:
    print ("list match")
else:
    print ("list dont")

print("this is even list {}".format(even))

# loop
combined_list = [odd, even]
print("combined lists {}".format(combined_list))

for i in combined_list:
    print(i)

    for j in i:
        print(j)

# iterator

my_list = iter(even)
print("Item in my list", next(my_list))
print("Item in my list", next(my_list))

# range

rangelist = list(range(10))
print("range list {}".format(rangelist))

evenrangelist = list(range(0, 10, 2))
print("range list {}".format(evenrangelist))

numbers = range(0, 10)
print("numbers", numbers)
myrange = numbers[::3]
print(myrange)

string = "abcdefgh"
print("printing string", string)
print("printing string", string.index('c'))
print("printing string", string[2])

print(range(0, 5, 2), range(0, 6, 2))
print (range(0, 5, 2) == range(0, 6, 2))
print("=" * 50)
print(type(range(0, 2)))
print(type(list(range(0, 2))))

# reversing the range
apple = range(0, 10)

for i in apple[::-1]:
    print(i)
print("-" * 10)
for i in range(10, 4, -1):
    print(i)

print("-" * 10)

apple = "My name is Gurpreet"
print(apple);
print("reverse apple range", apple[::-1])

# check

tea = range(0, 100, 2)
print("tea", tea)
print("tea", tea[::5])

# append
print("=" * 50)
a = "1,2,3"
print(type(a))
b = [1, 2, 3]
print(type(b))
c = (1, 2, 3)
print(type(c))

print("index 1 contains", a[1], b[1], c[1])
print(b.append(22))
print(b.pop(1))
print(b)

d = a, b, c
print("All in", d, type(d))

e = (a, b, c)
print("All in", e, type(e))

f = [a, b, c]
print("All in", f, type(f))

for i in f:
    print(i)
    print("-" * 5)
    for j in i:
        print(j)

# string
print("--" * 4)
st = "1,2,3"
print(st[1])
st = st +">"
print(st)


#Diff

a=[1,2,3]
b=[1,5,6,7]
print("Add",a+b)


even = [10,2, 4, 6, 8]
odd = [1, 3, 5, 7]

print(even);
even.sort()
print(even);
even.sort(reverse=True)
print(even);

if even==odd:
    print ("list match")
else:
    print ("list dont")

print("this is even list {}".format(even))

#loop
combined_list=[odd,even]
print("combined lists {}".format(combined_list))

for i in combined_list:
    print(i)

    for j in i:
        print(j)


#iterator

my_list=iter(even)
print("Item in my list",next(my_list))
print("Item in my list",next(my_list))

#range

rangelist=list(range(10))
print("range list {}".format(rangelist))

evenrangelist=list(range(0,10,2))
print("range list {}".format(evenrangelist))

numbers=range(0,10)
print("numbers", numbers)
myrange=numbers[::3]
print(myrange)

string="abcdefgh"
print("printing string",string)
print("printing string",string.index('c'))
print("printing string",string[2])

print(range(0,5,2),range(0,6,2))
print (range(0,5,2)==range(0,6,2))
print("="*50)
print(type(range(0,2)))
print(type(list(range(0,2))))

#reversing the range
apple=range(0,10)

for i in apple[::-1]:
    print(i)


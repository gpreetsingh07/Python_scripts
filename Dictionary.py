cars={1:"Suzuki", 2:"Honda", 3:"Accura", 4:"Ferrari"}

print(cars)
print(cars[2])
print(cars.values())
print(cars.keys())

for i in cars:
    print(cars.get(i))
    if cars.get(i)=="Honda":
        break


#another way to loop dictionary
print("-"*10)

for j in cars:
    print(cars[j])


#create list from dictionary keys

list=cars.keys()
print("list from cars",list)
list.sort(reverse=True)
print("list from cars",list)

for i in list:
    print(cars[i])

#another way to sort
list=sorted(cars.keys())
list=list[::-1]
print(list)

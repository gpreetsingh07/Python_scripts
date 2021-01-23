#convert to binary using :b

i=range(0,10)
for j in i:
    print("{}{} is {:b}".format("Binary of ",j,j))


i=range(100,110)
for j in i:
    print("{}{} is {:X}".format("Hex of ",j,j))
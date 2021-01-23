#using open
file=open('/Users/gps/IdeaProjects/Python_scripts/readme.txt','r')

for i in file:
    print(i)
file.close()

print("#"*10)

#using with open as file
with open('/Users/gps/IdeaProjects/Python_scripts/readme.txt','r') as file:
    i=file.readlines()
    #k=file.readline()

for j in i:
    print(j[::-1])
print("--"*10)



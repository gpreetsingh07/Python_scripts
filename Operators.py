x=10

x+=20
print(x)
x-=20
print(x)
x/=2
print(x)
x**=2
print(x)
x%=7            #modolu
print(x)

x=''
a="1,2,3,4,5"
print(a)

for i in a:
    if i in '0123456789':
        x=x+i
        print(x)
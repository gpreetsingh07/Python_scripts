print("""hello this is python string
using
triple quotes.''' it allows to write freely""");

print("{} has {} days".format("jan", "31"));

print("Printing table of 2");
for i in range(1, 100):
    print('{} x {} = {}'.format(2, i, 2 * i))

names = input("What is your name")
age = int(input("what is your age {}".format(names)));
print(age);


if age>5:
    print("Age is greater")
elif age<5:
    print("Age is less")
else:
    print("Dont know age")

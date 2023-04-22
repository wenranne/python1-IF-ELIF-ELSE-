#here you will see anything with comments explained
#what is the program: the program will understand that a is bigger than b, or b is bigger than a, or a = b.
#what we are going to use: in here mainly we use IF/ELIF/ELSE statements





print("the program will ask you enter numbers for a and b")
a = int(input("enter a number for 'a': ")) # "a = variable", int = "integer" input = "input is using for letting the user input their value"
b = int(input("enter a number for 'b': "))

if a > b:
    print("a is bigger than b")
elif b > a:
    print("b is bigger than a")
elif a == b:
    print("a is equal to b")

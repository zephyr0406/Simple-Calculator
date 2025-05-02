# my simple calculator


#add
def add(a, b):
    c = a + b
    print(c)
    return c


#subtract
def subtract(a, b):
    c = a - b
    print(c)
    return c


#multiply
def multiply(a, b):
    c = a * b
    print(c)
    return c


#divide
def divide(a, b):
    c = a / b
    print(c)
    return c


#taking input from user
print("select your choices")
print("1. Add")
print("2. subtract")
print("3. Multiply")
print("4. Divide")

while True:

    #taking input for operation from user

    z = input("for process select(1/2/3/4):   ")

    if z in ("1", "2", "3", "4"):
        try:
            x = int(input("enter number1: "))
            y = int(input("enter number2: "))
        except ValueError:
            print("try again")

        # add function
        if (z == "1"):
            add(x, y)
        # subtract function
        elif (z == "2"):
            subtract(x, y)
        # multiply function
        elif (z == "3"):
            multiply(x, y)
        #divide function
        elif (z == "4"):
            divide(x, y)

        #repeat process if needed
        new_turn = input("Do you want to a new calculation(y/n): ")
        #end process
        if (new_turn == "n"):
            print("Session Ended at code = 0")
            break
        #repeat the loop
        elif (new_turn == "y"):
            continue

#exceptional error
else:
    print("Error 101")

# long winded way of asking the user for a number and then telling them if it's even or odd
def main():
    num = int(input("give me a number? "))
    if is_even(num):
        print("Even")
    else:
        print("Odd")

def is_even(n): #n refers to the "number" given in the input variable
    if n % 2 == 0:
        return True
    else:
        return False
    
#another way to write is_even()
#def is_even(n):
#    return True: if n % 2 == 0 else False

main()

#simple multiplying function that asks the user for a number, then multiplies it by the given amount
x = int(input("x is? "))
y = int(input("y is? "))

def multiply():
    return x * y

print(multiply())
print(f"{multiply():,}") # the f"{}" is used to format the result in a certain way (in this example with :, commas) to make it easier to read

# a simple functino to ask a user their name and how you can manipulate how it is displayed; examples are title() capitalize() upper() strip()

def your_name():
    name = input("What's your name? ").title()
    print("Hello, ", name)

your_name()
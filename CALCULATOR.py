#NEW PROJECT CALCULATOR
#Helps to Calculation logic
def add(x, y):
    return x + yclear


def sub(x, y):
    return x - y

def multiply (x, y):
    return x * y

def dev(x, y):
    return x / y

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

#Taking input from the user

sel = int(input("Select operations form 1, 2, 3, 4 :"))  
    
num_1 = int(input("ENTER THE FIRST NUMBER: "))
num_2 = int(input("ENTER THE SECOND NUMBER: "))

if sel == 1:
    print(num_1, "+", num_2, "=",
                    add(num_1, num_2))
    
elif sel ==2:
    print(num_1, "-", num_2, "=",
                    sub(num_1, num_2))
elif sel == 3:
    print(num_1, "*", num_2, "=",
                    multiply(num_1, num_2))
    
elif sel == 4:
    print(num_1, "/", num_2,
                    dev(num_1, num_2))
    
    
else: 
        print("invalid input")
    
    

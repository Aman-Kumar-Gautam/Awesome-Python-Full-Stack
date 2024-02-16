# installation on Windows
# website www.python.org
# Download the latest version of python3
# Note during installation don't forget to add to the path
# install any ide for python (like: pycharm, atom, vscode)
# or go with python IDLE inbuilt

# 1.1.3 variable in python

# There are 3 types of variable
# 1. Integer value
x = 5

# 2. Float
y = 5.5

# 3. String
z = " Hii Pythons"

# 4. Boolean
a = True
print(x, y, z, a)

# 1.3.4 Built-in object types
# to  check types of variable (:- use type() keywords)
print(type(x))
print(type(y))
print(type(z))
print(type(a))

# 1.4 Number conversion
x = float(x)
print(type(x))
y = int(y)
print(type(y))


# Python Operator's
# 1. Binary Operator
"""
$ - And 
| - Or
^ - XOR
~ - NOT
<< - shift left
>> - shift right

"""

# 2  Comparison Operator's
"""
(= =) - [Equal]
(! =) - [Not Equal]
(>)   - [Greater than]
(<)   - [Less than]
(>=)  - [Greater than or equal too]
<=    - [less than or equal too]

"""


# 3  Operators' Precedence
"""
1. "**"                = Experimentation ( raise to the Power)

2. "~ + , -"           = Complement unary plus and minus
3. " *, /, %, //, = "  = Multiply, Divide, Module, Floor, Division, Equal too
4. " +, -"             = Addition and Subtraction
>> , <<                = right or left bitwise sift
&                      = Bitwise And 
^,|                    = Bitwise exclusive OR and Regular OR
<= , >=                =
<, > , ==, !           =
is , is not            =
in , not in            =
not , or , and         =
"""
# 4  Ternary Precedence
"""
[on True] if [Expression] else [on False]
"""
# 1.5 Control structure
# 1.5.1 if-else
"""
if condition is true:
    run this block:

elif check this condition:
    run this block

else:
    run this block
"""
# Question Zig-Zag
def Zig_Zag(n):
    if n % 3 == 0 and n % 5 == 0:
        print(" ZigZag")

    elif n % 5 == 0 and n % 3 != 0:
        print("Zag")

    elif n % 3 == 0 and n % 5 != 0:
        print("Zig")
    else:
        print(" No Zig and No Zag")


n = int(input("Input:  "))
Zig_Zag(n)

# 1.5.2 while loop
"""
while (condition not meet this step ):
    do this implementation on code
"""
def User_table(n):
    i = 1
    while i <= 10:
        print(n, "*", i, "= ",i*n)
        i += 1

n = int(input(" Input: "))

User_table(n)

# 1.5.3 for loop
"""
for i in run program till reached this situation(x):
"""
data = [1, 2, 3, 4, 5, 7, 8, 9, 10]
for i in range(len(data)):
    print(i)
# for loops comes with the 2 special feature

    # 1. range -- It returns the object that produced sequence of integer*
    # range(Start, Stop, Step)


    # 2. enumerate --
    # enumerate(iterable, start=0)


# 1.6 Function
# def -- In creation function we have to use def keyword
def function():
    print("Hello, In The function")


function()
# for running any function we have to call that function using (Function Name)
# or make any object and then to call the object

def fun():
    print(""" Using Object
    calling function
    """)


a = fun()


print(a)



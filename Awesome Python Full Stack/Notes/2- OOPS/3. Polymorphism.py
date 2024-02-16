"""
# Polymorphism:::
# Polymorphism defines the ability to take different forms .Polymorphism in Python allows us to define methods in the
# child class with the same name as defined in their parent class.

# What is Polymorphism?
# 1: Polymorphism in Python
# 2: Polymorphism with Function and Objects
# 3: Polymorphism with Class Methods
# 4: Polymorphism with Inheritance


# What is Polymorphism?
# Polymorphism is taken from the Greek words Poly(many) and morphism(forms).It means that the    same   function    name
# can    be    used    for different types.This makes programming more intuitive and easier.    In    Python, we
# have    different    ways    to    define    polymorphism.So


#   let’s    move    ahead and see    how    polymorphism    works in Python. Polymorphism in Python use polymorphism
#   in Python.You    can use    different function, class methods or objects to define polymorphism.
#   So, let’s move ahead and have a look at each of these methods in detail.

# Let’s take an example and create a function called “func()” which will take an object which we will name “obj”.Now,
# #let’s give the function something to do that uses the ‘obj’ object we passed to it.In this case,let’s    call    the
# methods    type() and color(), each
# of which is defined in the two classes ‘Tomato’ and ‘Apple’.Now, you have to create instantiations of
#  both    the ‘Tomato’ and ‘Apple’ classes if we don’t    have them    already:
"""


class Tomato:
    def type(self):
        print("Vegetable")

    def color(self):
        print("Red")


class Apple:
    def type(self):
        print("Fruit")

    def color(self):
        print("Red")


def func(obj):
    obj.type()
    obj.color()


obj_tomato = Tomato()
obj_apple = Apple()
func(obj_tomato)
func(obj_apple)
# Output:

# Vegetable
# Red
# Fruit
# Red
# Polymorph is with Class Methods Python uses two
# different class types in the same way.Here, you have to create a for loop that iterates through a tuple of objects.
# Next, you have to call the methods without being concerned about which class type each object is.
# #We assume that these methods actually exist in each class.Here is an example to show polymorphism with class:




class India:
    def capital(self):
        print("New Delhi")

    def language(self):
        print("Hindi and English")


class USA():
    def capital(self):
        print("Washington, D.C.")

    def language(self):
        print("English")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
country.language()

# Output:

# New
# Delhi
# Hindi and English
# Washington, D.C.
# English




# Polymorphism with Inheritance Polymorphism in python defines methods in the child
# class that have the same name as the methods in the parent class.In inheritance, the child class inherits the
# methods from the parent class.Also, it is possible to modify a method in a child class that it has inherited from
# the parent class.This is mostly used in cases where the method inherited from the parent class doesn't fit
# the child class.This process of re-implementing a method in the child class is known as Method Overriding.
# #Here is an example that shows polymorphism with inheritance:





class Bird:
    def intro(self):
        print("There are different types of birds")

    def flight(self):
        print("Most of the birds can fly but some cannot")


class Parrot(Bird):
    def flight(self):
        print("Parrots can fly")


class Penguin(Bird):
    def flight(self):
        print("Penguins do not fly")


obj_bird = Bird()
obj_parr = Parrot()
obj_peng = Penguin()

obj_bird.intro()
obj_bird.flight()

obj_parr.intro()
obj_parr.flight()

obj_peng.intro()
obj_peng.flight()
# Output:
#  here are different types of birds Most of the birds can fly but some cannot There are different types of bird Parrots
#  can fly There are many types of birds Penguins do not fly



# Encapsulation in python::
# 1 : Protected
# 2 : Private

# 3 Getter method
# 4 Setter method

"""
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can only be changed by an object’s method.
Those types of variables are known as private variables.
"""


# Python program to
# demonstrate protected members

# Creating a base class




class Base:
    def __init__(self):
        # Protected member
        self._a = 2


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a)

        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)




# Python program to demonstrate private members

# Creating a Base class




class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        super().__init__()
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)
print(obj1.c)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an Attribute Error as
# private member of base class
# is called inside derived class


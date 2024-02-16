"""
# 3 Inheritance:: Inheritance is a concept in the OOPS to code reusability The method of inheriting the properties of
parent class into a child class is known as inheritance.

# 1 :: Single Inheritance.
# 2 :: Multiple Inheritance.
# 3 :: Multilevel Inheritance.
# 4 :: Hierarchical Inheritance.
# 5 :: Hybrid Inheritance.
"""


class Parent:               # 1 :: Single Inheritance.

    def func1(self):
        print("this is function one")


class Child(Parent):

    def func2(self):
        print(" this is function two ")


ob = Child()
ob.func1()
ob.func2()




class Parent:                   # 2 :: Multiple Inheritance.

    def func1(self):
        print("this is function one")


class Parent2:
    def func2(self):
        print("this is function two")


class Child(Parent, Parent2):
    def func3(self):
        print("this is function three")


ob = Child()
ob.func1()
ob.func2()
ob.func3()



class Parent:                   # 3 :: Multilevel Inheritance.

    def func1(self):
        print("this is function one")


class Child(Parent):

    def func2(self):
        print("this is function two")


class Child2(Child):

    def func3(self):
        print("this is function three")


ob = Child2()
ob.func1()
ob.func2()
ob.func3()


class Parent:                       # 4 :: Hierarchical Inheritance.

    def func1(self):
        print("this is function one")


class Child(Parent):
    def func2(self):
        print("this is function two")


class Child2(Parent):
    def func3(self):
        print(" this is function three")

ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()



class Parent:                       # 5 :: Hybrid Inheritance.

    def func1(self):
        print("this is function one")


class Child(Parent):
    def func2(self):
        print("this is function two")


class Child1(Parent):
    def func3(self):
        print(" this is function three")


class Child2(Child1, Child):
    def func4(self):
        print(" this is function four")


ob = Child2()
ob.func1()
ob.func2()
ob.func3()
ob.func4()
ob1 = Child()
ob1.func1()
ob1.func2()
ob2 = Child1()
ob2.func1()
ob2.func3()

# Python Super() Function Super function allows us
# to call a method from the parent


class Parent:
    def func1(self):
        print("this is function one")


class Child(Parent):
    def func2(self):
        super().func1()
        print("this is function two")


ob = Child()
ob.func2()
ob.func1()

# Python  Overriding Method
# below.


class Parent:
    def func1(self):
        print("this is parent function")


class Child(Parent):
    def func1(self):
       # super(Child, self).func1()
        print("this is child function")


ob = Child()
ob.func1()



# The functionality of the parent class method is changes by overriding the same method in the child class.
# Inheritance is one of the most important concept of OOP.It provides code reusability, readability and transition of
# properties which helps in optimized and efficient code building.


"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    store_name = "Some Restaurant"  # Class variable
    def __init__(self, name, employee_id): # Constructor
        self.name = name  # instance variable
        self.employee_id = employee_id # Instance variable

    def display_info(self):  #Display method
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Store: {self.store_name}")
    pass


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    store_location = "Downtown"  # New class variable
    def __init__(self, name, employee_id, position, salary):  # Constructor
        super().__init__(name, employee_id)  # Call parent constructor
        self.position = position  # New instance variable
        self.salary = salary  # New instance variable

    def display_info(self):  # Override method
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Store: {self.store_name}, "
              f"Position: {self.position}, Salary: {self.salary}, Location: {self.store_location}")
    pass


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    person1 = ChildClass("John", 101, "Manager", 60000) # Creating first object of ChildClass
    person2 = ChildClass("Jane", 102, "Chef", 50000) # Creating second object of ChildClass

    print (ChildClass.store_name)  # Accessing class variable through class

    print(person1.store_name)  # Accessing class variable through object

    person1.is_servesafe_certified = True  # Adding new attribute to person1

    print(person1.__dict__)  # Displaying person1's namespace
    print(person2.__dict__)  # Displaying person2's namespace

    print(ChildClass.__dict__)  # Displaying class namespace

"""
Terminal Output:

=== Namespace Demonstration ===
TODO: Implement namespace demonstration
Some Restaurant
Some Restaurant
{'name': 'John', 'employee_id': 101, 'position': 'Manager', 'salary': 60000, 'is_servesafe_certified': True}
{'name': 'Jane', 'employee_id': 102, 'position': 'Chef', 'salary': 50000}
{'__module__': '__main__', 'store_location': 'Downtown', '__init__': <function ChildClass.__init__ at 0x10234f670>, 'display_info': <function ChildClass.display_info at 0x10234f700>, '__doc__': None}
"""


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    person1 = ChildClass("John", 101, "Manager", 60000)  # Creating an object of ChildClass
    person1.skills = ["Leadership", "Communication"]  # Adding nested mutable data

    shallow_copy_person1 = copy(person1)  # Creating a shallow copy

    deep_copy_person1 = deepcopy(person1)  # Creating a deep copy

    person1.skills.append("Problem Solving")  # Modifying the original object's nested data

    print("Original object:", person1.__dict__)  # Displaying original object
    print("Shallow copy:", shallow_copy_person1.__dict__)  # Displaying shallow copy
    print("Deep copy:", deep_copy_person1.__dict__)  # Displaying deep copy

"""
Terminal Output:

=== Copy Demonstration ===
TODO: Implement shallow copy and deep copy demonstration
Original object: {'name': 'John', 'employee_id': 101, 'position': 'Manager', 'salary': 60000, 'skills': ['Leadership', 'Communication', 'Problem Solving']}
Shallow copy: {'name': 'John', 'employee_id': 101, 'position': 'Manager', 'salary': 60000, 'skills': ['Leadership', 'Communication', 'Problem Solving']}
Deep copy: {'name': 'John', 'employee_id': 101, 'position': 'Manager', 'salary': 60000, 'skills': ['Leadership', 'Communication']}
"""

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    parent_object = ParentClass("John", 101) # Creating an object of ParentClass
    parent_object.display_info()  # Calling method from ParentClass


    print("\nTODO: Create and test your child object")
    child_object = ChildClass("Jane", 102, "Chef", 50000) # Creating an object of ChildClass
    child_object.display_info() # Calling overridden method from ChildClass

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
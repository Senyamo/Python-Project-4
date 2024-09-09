class Person:
    def __init__(self, name, age, gender):
        self.name = name  
        self.age = age   
        self.gender = gender  

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        # Method to introduce the person
        print(f"Hi, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

#code with output
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Create an instance
person1 = Person("Senyamo Molefe", 33, "Male")

# Call the method
person1.introduce()

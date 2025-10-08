# defining a class
class Employee:
    def __init__(self,name,age):
        # instance variables
        self.name = name # creates and attrinute names and assigns it to value of the name parameter
        self.age = age

# we will build on a dog class
class Dog:
    # class variable (have same value for all class instances)
    species = "Canis familiaris"
    def __init__(self,name,age,breed):
        # instance variables
        self.name = name # creates and attrinute names and assigns it to value of the name parameter
        self.age = age
        self.breed = breed
    
    
    # instance methods
    def description(self):
        return f"{self.name} is {self.age} years old."
    def speak(self,sound):
        return f"{self.name} says {sound}"
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    
# instantiate a class
mile = Dog("Miles",3,"kiimani")
caro = Dog("caroline",8,"bosco")


print(mile.name)
print(caro.species)
print(mile.species)
print(caro.description())
print(mile.speak("woof wooof!"))
print(mile)


#### 1. INHERITANCE ####
class Parent:
    speaks = ['English']
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")

class JackRussellTerrier(Dog):
    def speak(self, sound="Alafu"):
        return f"{self.name} says {sound}"
jack = JackRussellTerrier("miles",4,"bosco")
print(jack.speak())


##### 2 : POLYMORPHISM ####
# similar method names behaving differently (you’ve partially shown it with overridden speak()).
class Cat:
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return f"{self.name} says Meow!"

class Cow:
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return f"{self.name} says Moo!"
    
animals = [Cat("Whiskers"),Cow("Bestie")]
for animal in animals:
    print(animal.speak()) # same method, different behaviors
    

##### 3. ABSTRACTION #####
from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started.Vroom vroom"
    
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started. Braap!"

# car = Vehicle - this will throw an error - Can't instantiate abstract class

mycar =Car()
my_bike = Motorcycle()
print(mycar.start_engine())
print(my_bike.start_engine())

##### 4 . ENCAPSULATION ###
# Encapsulation is the bundling of data and the methods that operate on that data within one unit — a class.
# It also means restricting direct access to some of an object’s components, which is often done by marking them as private/protected.
class BankAccount:
    def __init__(self,owner,balance):
        # instance variables (encapsulated data)
        self.owner = owner
        self._balance = balance # private variable
        
        # instance methods (encapsulated behavior)
    def deposit(self,amount):
        if amount >0:
            self._balance +=amount
    
    def withdraw(self,amount):
        if 0 <amount <=self._balance:
            self._balance -=amount
            
    def get_balance(self):
        return self._balance
            
        
# Alternative to Duck typing
# With this strategy, you’ll rely on the base class to enforce the necessary interface. 
# Additional protection
# You have a base class that enforces a given API in its subclasses. 

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self) -> None:
        ...

    @abstractmethod
    def swim(self):
        raise NotImplementedError("swim() must be implemented")
    
    @abstractmethod
    def fly(self):
        raise NotImplementedError("fly() must be implemented")
    


class Duck(Animal):
    def swim(self):
        print("Duck swimming")

    def fly(self):
        print("Duck flying")

class Whale(Animal):
    def swim(self):
        print("Whale swimming")


for animal in [Duck(), Whale()]:
    animal.swim()
    animal.fly()

# TypeError: Can't instantiate abstract class Whale without an implementation for abstract method 'fly'


# That’s it! You’ve replaced duck typing with ABCs. Note that in this case, your classes are coupled with the base class. 
# This can be a limitation because you won’t be able to reuse one of your classes in a different project unless you also take the Vehicle class with you.
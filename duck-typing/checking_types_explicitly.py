# This alternative is more restrictive and consists of making sure that an object is of a given type or
#  has the required methods before you can use it in your code.

# Even though checking the type of an object before using it can be a good solution in some cases, it’s not the best approach. 
# One of Python’s main characteristics is its flexibility regarding types, and checking types all the time isn’t a very flexible thing to do.

class Duck:
    def swim(self):
        print("Duck swimming")

    def fly(self):
        print("Duck flying")

class Whale:
    def swim(self):
        print("Whale swimming")

for animal in [Duck(), Whale()]:
    if isinstance(animal, Duck):
        animal.swim()
        animal.fly()

for animal in [Duck(), Whale()]:
    if hasattr(animal, "swim") and hasattr(animal, "fly"):
        animal.swim()
        animal.fly()
# Typical duck typing with custom classes
# +: classes are decoupled, simplicity, 
# -: Potential runtime errors, Lack of explicitness

# class BaseClass:
#     def swim(self):
#         raise NotImplementedError(
#             "Subclasses must implement this method"
#         )

#     def fly(self):
#         raise NotImplementedError(
#             "Subclasses must implement this method"
#         )

class Duck:
    def swim(self):
        print("Duck swimming")

    def fly(self):
        print("Duck flying")

class Whale:
    def swim(self):
        print("Whale swimming")


# def do_something(animals: BaseClass): we traded duck typing for inheritance
def do_something(animals):
    for animal in animals:
        animal.swim()
        animal.fly()


do_something([Duck(), Whale()])
# Duck swimming
# Duck flying
# Whale swimming
# AttributeError: 'Whale' object has no attribute 'fly'



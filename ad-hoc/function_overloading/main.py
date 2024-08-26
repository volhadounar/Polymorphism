
from functools import singledispatch

class Human:
    def __repr__(self): 
        return "Привет"

class Dog:
    def __repr__(self):
        return "Гав-гав"

class Cat:
    def __repr__(self): 
        return "Мяу-мяу"


@singledispatch
def fun(arg): # ф-ия вызывается по умолчанию если типа для аргумета не нашлось
    print("Hello world!")

@fun.register
def _(arg:Human):
    print(f"Hello Human {arg}")

@fun.register
def _(arg:Dog, verbose=False):
    print(f"Hello dog {arg}")

@fun.register
def _(arg:Cat, verbose=False):
    print(f"Hello cat {arg}")

# понимает какую вызвать по аннотациям типов
fun("some") #call default value
fun(Dog()) # call with dog
fun(Human()) # call with human
fun(Cat()) # call with cat
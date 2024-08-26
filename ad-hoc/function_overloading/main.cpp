#include <iostream>

// Overloading - not the fundamenal feature of type system, 
// specify a common interface (polymorphic functions) for  concrete types
// polimorphyc functons functions involkation depend on the input parameters
// from the top as function works generically over several input types
// but they are considered by the compiler entirely distinct functions
// Can it be implemented in the dynamically typed languages? the correct function that needs to be invoked might only be determinable at run time.


class Human {};
class Dog {};
class Cat {};

// TODO: Write hello() function
void hello() { std::cout << "Hello, World!\n"; }

// TODO: Overload hello() three times
void hello(Human human) { std::cout << "Hello, Human!\n"; }
void hello(Dog dog) { std::cout << "Hello, Dog!\n"; }
void hello(Cat cat) { std::cout << "Hello, Cat!\n"; }

// TODO: Call hello() from main()
int main()
{
    hello();
    hello(Human());
    hello(Dog());
    hello(Cat());
}
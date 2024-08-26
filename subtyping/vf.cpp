#include <cassert>
#include <string>
#include <iostream>

// to restrict the range of types that can be used in a particular case of polymorphism
// it uses the nominal static type system

class Animal {
public:
    virtual std::string Talk() const {return "ggg";}
};

class Dog: public Animal {
public:
 std::string Talk() const;
};

std::string Dog::Talk() const {return "Woof";}


void letsHear(Animal* pet) {
    std::cout << pet->Talk();
    // (*(pet->vptr[0]))(pet)
}

void letsHear(Animal pet) {
    std::cout << pet.Talk();
    // (*(pet->vptr[0]))(pa)
}

int main(){
    Dog* dog = new Dog();
    assert(dog->Talk() == "Woof");
    letsHear(dog);

    Dog dog2;
    letsHear(dog2);
}
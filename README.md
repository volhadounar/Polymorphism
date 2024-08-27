Prerequisites:

	• Type system
	• Intro to Polymorphism
	• Parametric polymorphism
	• Subtyping polymorphism
	• Raw polymorphism
	• Duck typing
	• Duck typing vs Type Hints

Type system

Major categories of type system:

• Static vs. dynamic
• Manifest vs. inferred
• Nominal vs. structural
• Duck typing

Intro to Polymorphism

Polymorphism means 'assuming many forms'.
There are many forms of polymorphism. The major forms are:
	• Ad-hoc or function overloading, operator overloading
	• Parametric
	• Subtyping or inclusion polymorphism
	• Duck typing


The concept is borrowed from a principle in biology.
Polymorphism, as related to genomics, refers to the presence of two or more variant forms of a specific DNA sequence that can occur among different individuals or populations.


Polymorphism allows to write a common code that acts on values of multiple types.


We can divide polymorphism into 2 groups:

	1) Ad-hoc 
 

Polymorphic functions define common interface for arguments of concrete types.
Simply put, 'the different code gets executed when function invocations happen'.
It can be achieved with C++ and Python for example.
In dynamically types languages at run time  and statically typed languages at compile time.

	2) Universal

Polymorphism uses 'Type system' to write reusable code.
Define a common interface without specifying concrete types.
Instead use abstract symbols, or the supertype.

The function or data type is allowed to be written generically and handle values uniformly without depending on their type.
Universal Polymorphism is about writing the code which is common for different acceptable arguments.

It can be achieved by generic programming, subtyping, virtual functions.

Parametric polymorphism
Can be achieved with generic programming. In languages with static type safety.
We do not restrict the range of types that can be used in particular case of polymorphism.

Subtyping
Subtyping allows a function to be written to take an object of a certain type T, but also work correctly, if passed an object that belongs to a type S that is a subtype of T (according to the Liskov substitution principle).

Row polymorphism
Is a similar but distinct concept from subtyping, it deals with structural types.
Structural type system is a class of type system in which type compatibility and equivalence are determined by the type's actual structure or definition and not by other characteristics such as its name or place of declaration.

Structural type systems

Duck typing is similar to, but distinct from, structural typing. Structural typing is a static typing system that determines type compatibility and equivalence by a type's structure, whereas duck typing is dynamic and determines type compatibility by only that part of a type's structure that is accessed during runtime.


https://en.wikipedia.org/wiki/Type_system

Duck typing:

The feature of this type of polymorphism is that objects don't have to inherit from a common superclass.
You just need to decide which methods and attributes a particular class has, and objects will share the same behavior.

What it does? Not what is it? The focus is on actions.

+: flexibility (use objects interchangably, do not depend on their types)
Simplicity, easier prototyping

-: potential runtime errors,  maintanance issues-Behavior changes in certain objects may impact other parts of the code, making it harder to maintain, reason about, and debug.


Duck typing vs/with Type Hints
…

References:

[https://realpython.com/duck-typing-python/#:~:text=Duck%20typing%20is%20a%20type,adhere%20to%20some%20common%20interface.](https://realpython.com/duck-typing-python/#:~:text=Duck%20typing%20is%20a%20type,adhere%20to%20some%20common%20interface.)

https://en.wikipedia.org/wiki/Type_system

https://en.wikipedia.org/wiki/Polymorphism_(computer_science)

https://realpython.com/python-protocol/

https://levelup.gitconnected.com/hidden-power-of-polymorphism-in-python-c9e2539c1633

https://realpython.com/python-protocol/#:~:text=Since%20Python%203.8%2C%20the%20static,of%20a%20given%20structural%20type.&text=In%20this%20code%2C%20you%20define,Protocol%20.s


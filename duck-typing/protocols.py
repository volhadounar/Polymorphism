# https://realpython.com/python-protocol/#:~:text=Since%20Python%203.8%2C%20the%20static,of%20a%20given%20structural%20type.&text=In%20this%20code%2C%20you%20define,Protocol%20.s

# Custom protocol
from typing import Protocol

class Adder(Protocol):
    def add(self, x: float, y: float) -> float:
        ...

class IntAdder:
     def add(self, x: int, y: int) -> int:
        return x + y

def add(adder: Adder) -> None:
    print(adder.add(2, 3))

add(IntAdder())

# error: Argument 1 to "add" has incompatible type "IntAdder";
#     expected "Adder"  [arg-type]
# adder_v2.py:17: note: Following member(s) of "IntAdder" have conflicts:
# adder_v2.py:17: note:     Expected:
# adder_v2.py:17: note:         def add(self, x: float, y: float) -> float
# adder_v2.py:17: note:     Got:
# adder_v2.py:17: note:         def add(self, x: int, y: int) -> int
# Found 1 error in 1 file (checked 1 source file)

# Generic Protocol

from typing import Protocol, TypeVar

T = TypeVar("T", bound=int | float)

class Adder(Protocol[T]):
    def add(self, x: T, y: T) -> T:
        ...

class IntAdder:
    def add(self, x: int, y: int) -> int:
        return x + y

class FloatAdder:
    def add(self, x: float, y: float) -> float:
        return x + y

def add(adder: Adder) -> None:
    print(adder.add(2, 3))

add(IntAdder())
add(FloatAdder())
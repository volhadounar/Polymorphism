# In the early stages of Python’s type hints, the system was mainly nominal.
# The type-hinting system continued to evolve, and now it also supports a structural type system 
# -  class can replace another if both have the same structure.
# Since Python 3.8, the static type checkers started to support structural subtyping, 
# which means that they check whether objects are of a specific nominal type and also whether they meet the requirement to be of a given structural type.

def mean(grades: list | tuple | set) -> float:
    return sum(grades) / len(grades)


mean([4, 3, 3, 4, 5])
mean((4, 3, 3, 4, 5))


from collections.abc import Collection
# Collection - ABC for sized iterable container classes as predefined protocol

# provide a generic type hint
def mean(grades: Collection) -> float:
    return sum(grades) / len(grades)




## Animal is-a object, because all animals are objects
class Animal(object):
    pass

## Dog is-a Animal; Dog is built on the Animal class
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name; Dogs reference names
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name
        # Should pull name into Animal

# Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## Parent class __init__ call
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## Jeeves is-a Cat
jeeves = Cat("Jeeves")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet with value jeeves
mary.pet = jeeves

## Frank is-a Employee
frank = Employee("Frank", 1200)

## Frank has-a pet with value rover
frank.pet = rover

frank.unknown = "unknown"

print frank
print frank.unknown # Objects can be made to deviate from their class specifications

## flipper is-a Fish
flipper = Fish()

print flipper

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

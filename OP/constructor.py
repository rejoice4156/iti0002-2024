"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Person constructor."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Student constructor."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    print(Empty)

    # 3 x person usage
    Person.firstname = "John"
    Person.lastname = "Wayne"
    Person.age = 35
    print(Person.firstname, Person.lastname, Person.age)

    # 3 x student usage
    student = Student("Lennart", "Poettering", 43)
    print(student.firstname, student.lastname, student.age)
    student = Student("Lisa", "Simpson", 10)
    print(student.firstname, student.lastname, student.age)
    student = Student("Bart", "Simpson", 12)
    print(student.firstname, student.lastname, student.age)

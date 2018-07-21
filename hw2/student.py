class student:
    def __init__(self, name, gpa, age):
        self.name = name
        self.gpa = gpa
        self.age = age

    def __str__(self):
        return "Student: {}; GPA: {}; Age: {}".format(self.name, self.gpa, self.age)

    def __lt__(self, other):
        if (self.gpa != other.gpa):
            return self.gpa < other.gpa
        else:
            if (self.name != other.name):
                return self.name < other.name
            else:
                return self.age < self.age

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __hash__(self):
        # Reference: https://stackoverflow.com/questions/4005318/how-to-implement-a-good-hash-function-in-python
        return hash((self.name, self.gpa, self.age))


def main():
    s1 = student("Jack", 3.6, 20)
    s2 = student("James", 3.7, 20)
    s3 = student("Mike", 3.6, 21)
    s4 = student("Jason", 3.5, 20)
    s5 = student("May", 3.5, 21)

    students = [s1, s2, s3, s4, s5]

    # sorted()
    students_sorted = sorted(students, key=lambda x: x.gpa)
    for s in students_sorted:
        print(s)

    # test using dict()
    # https://docs.python.org/2/library/stdtypes.html?highlight=__dict__#object.__dict__
    print(dict(s1.__dict__))


if __name__ == "__main__":
    main()
class student:
    def __init__(self, name, gpa, age):
        self.name = name
        self. gpa = gpa
        self.age = age

    def __str__(self):
        return "Student: "+self.name+"; GPA: "+self.gpa+"; Age: "+self.age

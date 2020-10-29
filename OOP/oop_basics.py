# Hove you ever seen something loke this
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    
    def bark(self):
        print('woof woof')

# then the concept used is Object Oriented programming (OOP)
# In OOP you will heat a lot about classes, objects and mehtods.
# well do not worry as the definitions are provided below
# classes defines the way in which an object can interact with one another so classes basically are just designs 
# An object is an instance of a class 
# Take for example, you have an  object lets say a car.
# a car will have both attributes and behaviour
# Now lets bring that into OOP concept 
# from the given example, we could see that a car definitely will have a design which is the shape right(now in  oop we call it class) 
# and the models pr brands will be the object.
# now each model will have different features unique to it thats where attributes and methods comes in 
# an attributes is a variable that gives in the necessary information about the design
# the method is function that is defined to perform specific functions(beahaviour)
# for example 
class Person:
    # this is our method
    def details(self):
        pass
     # you can absolutely define any function inside here

# we have our object here
p1 = Person()
# to print whatever function we define 
p1.details()
# we can have more than one object iln this class and each object is allocated a different memory
# also the size of an object depends on the following
# number of variables
# size of each variable
# allocation of this spaces is taken care of by the constructor
# the constructor is simply the function call (p1.details())
# also we could initialize a variable similar to the first instance given
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    
    def bark(self):
        print('woof woof')
# the __init__ method is the initiator
# you can absolutely give the data to be passed inside the init method 
# just to keep things minimal I'll just define a little more terminilogy and you should be able to grasp the other part as i've maintained proper commenting
# self: pointer
# vaiables in oop
# instance variable and class variable
# class variable is a variable that is general to all the methods and cannot be changed for a particular one (example here)
# an instance variable can be change during the function call
# also we have type of methods 
# instace method, class method and static method
# the example below is the first example I wrote few hours after starting OOP concept 
class Student:
    # class variable
    school = "Kunike International School"

    # instance method
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # class method
    @classmethod # note for class mehtod @classmethod decorator is used and in the method definition cls is passed as a parameter instead of self
    def get_school(cls) # cls is generally accepted that is why it is always used: 
        return cls.school

    # static method # for static mehtod @staticmethod attributor is used and when defining the function you may or may not pass a parameter 
    # static because it doesn't change, modify or do anything to our class
    @staticmethod
    def info():
        print("This is a Student class....")


digit = []
# just to practice collecting the input from the user, ypu can as well ,make it better cuz there are lots of stuffs that could be done just in one line
name = input('Enter student name: ')
print('Enter three numbers separed by a comma''\n')
number = input('Enter the numbers: ').strip()
# print(number)
passing_number = number.split(',')
print(passing_number)

for number in passing_number:
    if number == '':
        continue
    number = int(number)
    digit.append(number)

# print(digit)

converted = tuple(digit)

# print(converted)
# print(converted[0])

for i in converted:
    a = converted[0]
    b = converted[1]
    c = converted[2]

# student variable
# for instance
s1 = Student(a, b, c)
print('Average score for', name, 'is', s1.avg())
# for class
print(Student.get_school())
# for static 
Student.info()   

# Inner classes in python
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        # accessing the inner class inside outer class
        # self.lap = self.Laptop()


    def show(self):
        print(self.name, self.rollno)   
        # print(self.lap)
        # self.lap.show
 

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8gb" 


        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Khalid", 2)
# accessing the inner class outside the outer class
lap1 = Student.Laptop()
lap1.show()
s1.show()
# result printed below
 print(s1.lap.brand)

# using inheritance
# single level inheritance 
class A :

    def __init__(self):
        print('In A init')


    def feature1():
        print('Feature 1 is working')
    
    def feature2():
        print('Feature 2 is working')

class B(A):


    def __init__(self):
        # when B inherits features from A
        # super().__init__()
        print('In B init') 


    def feature3():
        print('Feature 3 is working')
    

    def feature4():
        print('Feature 4 is working')


class C :
    

    def __init__(self): 
        print("In C init")
# callilng the methods
a1 = A()

b1 = B()

# duck typing in python 
class Pycharm:
 
    def execute(self):
        print('Compiling...')
        print('Running...')


class Vscode:


    def execute(self):
        print('Spell Check...')
        print('Convention Check...')
        print('Compiling...')
        print('Running...')


class Laptop:


    def code(self,ide):
        ide.execute()


ide = Pycharm()

run1 = Laptop()

run1.code(ide)

ide = Vscode()

lap1 = Laptop()

lap1.code(ide)

# quick note
# when working with class variables, we could add a little more functionality to keep track of the counts
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person('Khalid')
print(Person.number_of_people)
p2 = Person('Tom')
print(Person.number_of_people)

# operator overloading 
class Student:

    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2


    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3


    def __gt__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        if m1 > m2 :
            return True 
        else:
            return False
            

    # to overwrite printing the address
    def __str__(self):
        return "{} {}" .format(self.m1, self.m2)


s1 = Student(58, 60)
s2 = Student(60, 65)

s3 = s1 + s2
 
print(s3.m1 + s3.m2)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')

# print(s1.__str__())
print(s1)



class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade


    def get_grade(self):
        return self.grade


class Course:
    # defined name of course and maximum numbers of students in a class 
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] 


    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False


    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
             
    
s1 = Student('Khalid', 18, 95)
s2 = Student('Muiz', 17, 89)
print(s1.age)
course = Course('Arts', 2)
course.add_students(s1)
course.add_students(s2)
print(course.students[0].grade) 
print(course.students[1].grade)
print(course.get_average_grade())
#Attributes and Methods
'''
1. What is an attribute?
- An attribute is a property that further defines a class.

2. What is a method ?
- A method is a function within a class which can access all the attributes of a class and perform a specific task.

3. What is a class attribute?
- Class attributes are attributes that are shared across all instances of a class.
- They are created either as a part of the class or by using className.attributeName

4. What is an instance attribute ?
- Instance attributes are attributes that are specific to each instance of a class.
- They are created using obbjectName.attributeName

5. How is self parameter handles ?
- The method call objectName.methodName() is interpreted as a className.methodName(objectName) and this parameter is referred to as
'self' in method definition.

6. What is an instance method?
- Methods that has the default parameter as the object are static methods. They are used to modify the instance attribute of a class.

7. What is a static method ?
- Methods that do not modify the instances attributes of a class are called instance methods. They can still be used to modify class attributes.

8. What is init() method?
- init() method  is the initializer in Python. It is called when an object is instantiated.
- All the attributes of the class should be initialized in this method to make your object a fully initialized object.

'''

class Employee():
    def __init__(self):
        self.name='Jagan'

    def empDetails(self):
        print(self.name)

empOne = Employee()
empOne.empDetails()

class Employee1():
    def __init__(self, name):
        self.name=name

    def empDetails(self):
        print(self.name)

empTwo = Employee1("jagadish")
empTwo.empDetails()

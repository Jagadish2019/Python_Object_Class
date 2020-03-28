'''Instance methods are methods of the class that make use of the self parameter to access and modify the instance
attributes of your class.'''

class Employee:
    def employeeDetails(self):
        self.name='Jagadish'

    @staticmethod # Its a decorator of python method where if you donot want to use the self parameter, staticmethod will come into picture
    def Greetings():
        print("Welcome to our organization!")


employee = Employee()
employee.employeeDetails()
print("The name from the function is ", employee.name)

employee.Greetings()


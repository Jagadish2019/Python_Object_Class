#What is self parameter and the reason why we use it?

class Employee:
    def employeeDetails(self):
        print("Hello from function")
        self.name='Jagan'
        print("The name is ", self.name)
        age=29
        print("The age is ", age)

    def anotherEmpDet(self):
        print("Printing the employee details from another function")
        print("The name is ", self.name)
        print("The age is ", age)

employeeOne= Employee()
employeeOne.employeeDetails()
Employee.employeeDetails(employeeOne)
employeeOne.anotherEmpDet()

# ''' Explanation : For the instance object employeeOne has the ability to print its attributes in the different methods. if and only of the self paramenter
# or the object name must be defined with the attribute. If its not defined then the life span of the attribute will be destroyed when the object is terminated
# and the attribute will not be available in the other function'''


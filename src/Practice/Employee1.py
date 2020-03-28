class Employee:
    numberOfWorkingHrs=45

#Creating an object for Employee class

employeeOne = Employee()

#printing the class variable value using the instance object of employee class
print(employeeOne.numberOfWorkingHrs)

Employee.numberOfWorkingHrs = 40

print(employeeOne.numberOfWorkingHrs)

employeeTwo = Employee()
employeeTwo.numberOfWorkingHrs = 50
print(employeeTwo.numberOfWorkingHrs)

print(employeeOne.numberOfWorkingHrs)
print(Employee.numberOfWorkingHrs)

employeeOne.name = 'Jagan'
print(employeeOne.name)

print(employeeTwo.name)
#Intance object when its created and while its executing it will first check the instance attributes are there or not. if its avaialablr
#then it will execute its value. If not it will execute the class attribute. in-case if class attribute also not present then the below error will
#thrown -> AttributeError: 'Employee' object has no attribute 'name'


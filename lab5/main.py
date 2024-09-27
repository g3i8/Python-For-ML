import os

welcomeList = ["new", "search", "delete", "show all", "exit"]
class Employee:
    idCount=0
    allEmployees=[]
    def __init__(self,name,salary,dep):
        Employee.idCount+=1
        self.id = Employee.idCount
        self.name=name
        self.salary=salary
        self.dep=dep
        Employee.allEmployees.append(self)

    def __repr__(self):
        return f'id= {self.id}, Name= {self.name}, salary= {self.salary}, dep= {self.dep}'

    @classmethod
    def newMethod(cls,employeeInfo):
        if len(employeeInfo) < 3:
            print("invalid entry!")
        else:
            if employeeInfo[1] == '' or not (employeeInfo[1].isnumeric()):
                salary = 0.0
            else:
                salary = float(employeeInfo[1])

            print("added new employee:")
            print(cls(employeeInfo[0],salary,employeeInfo[2]))


    @classmethod
    def searchMethod(cls, searchName):
        check = lambda emp: searchName and emp.name.lower().startswith(searchName)
        for emp in list(filter(check, cls.allEmployees)):
            print(emp)

    @classmethod
    def deleteMethod(cls, deleteName):
        index = 0
        while index < len(cls.allEmployees):
            emp = cls.allEmployees[index]
            if deleteName and emp.name.lower().startswith(deleteName):
                print("deleting employee:")
                print(emp)
                cls.allEmployees.pop(index)
            else:
                index += 1
    @classmethod
    def showMethod(cls):
        for emp in cls.allEmployees:
            print(emp)

Employee("ahmed ali",2000,'finance')
Employee("salma ahmed",3000,'HR')
Employee("amr ahmed",4000,'Eng')
Employee("ali mahmoud",5000,'HR')
#print(*Employee.all)


while 1:
    input()
    os.system('cls')

    # menu
    for (index, word) in enumerate(welcomeList):
        print(f'{index+1}-{word}')

    #progress
    process = input("enter process:")
    match process:
        case '1':
            information = input("enter name, salary, dep:").split(',')
            stripedInformation = list(map(str.strip, information))
            Employee.newMethod(stripedInformation)
            # new
        case '2':
            searchValue = input("search by first name:").lower().strip()
            Employee.searchMethod(searchValue)
            # search
        case '3':
            deleteValue = input("delete by first name:").lower().strip()
            Employee.deleteMethod(deleteValue)
            #delete
        case '4':
            Employee.showMethod()
            #show all
        case '5':
            print("bye")
            break
        case _:
            print("invalid process")
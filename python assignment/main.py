
import os
import pickle
#import csv


class Employee:
    idCount = 0
    allEmployees = []

    def __init__(self, name, salary, dep, id=None):
        if id is None:
            Employee.idCount = Employee.maxID() + 1
            self.id = Employee.idCount
        else:
            self.id = id
        self.name = name
        self.salary = salary
        self.dep = dep
        Employee.allEmployees.append(self)

    def __repr__(self):
        return f'id= {self.id}, Name= {self.name}, salary= {self.salary}, dep= {self.dep}'

    @classmethod
    def newMethod(cls, employeeInfo):
        if len(employeeInfo) < 3:
            print("invalid entry!")
        else:
            if employeeInfo[1] == '' or not (employeeInfo[1].isnumeric()):
                salary = 0.0
            else:
                salary = float(employeeInfo[1])

            print("added new employee:")
            print(cls(employeeInfo[0], salary, employeeInfo[2]))

    @classmethod
    def searchMethod(cls, searchName):
        check = lambda emp: searchName and emp.name.lower().startswith(searchName)
        for emp1 in list(filter(check, cls.allEmployees)):
            print(emp1)

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

    @classmethod
    def csvImport(cls,fileName):
        with open(fileName, 'r') as file:
            file.readline()
            for line in file:
                values = line.split(',')
                cls.newMethod(values)

        # with open(fileName, mode='r') as file:
        #     file.readline()
        #     csvFile = csv.reader(file)
        #     for line in csvFile:
        #         cls(line)

    @classmethod
    def importPickle(cls,fileName):
        try:
            with (open(fileName, "rb")) as pickleFile:
                restoredState = pickle.load(pickleFile)
                for key, value in restoredState.items():
                    cls(value[0], value[1], value[2], key)
        except:
            print("pickle file doesn't exist")

    @classmethod
    def exportEmployees(cls,fileName):
        with open(fileName, 'w') as file:
            for emp in cls.allEmployees:
                file.write(
                    f'id= {emp.id}, Name= {emp.name}, salary= {emp.salary}, dep= {emp.dep}')

    @classmethod
    def makeDeparttmentDict(cls):
        depDict = {}
        depDict = {emp.dep: [] for emp in cls.allEmployees}
        for emp in cls.allEmployees:
            depDict[emp.dep].append((emp.id, emp.name, emp.salary))
        return depDict

    @classmethod
    def exportDepartment(cls,depDict, fileName):
        with open(fileName, 'w') as file:
            for key, value in depDict.items():
                file.write(f"{key}\n")
                for val in value:
                    file.write(f"id= {val[0]}, Name= {val[1]}, salary= {val[2]}\n")

    @classmethod
    def exportPickle(cls,fileName):
        state = {}
        for emp in cls.allEmployees:
            state[emp.id] = (emp.name, emp.salary,emp.dep)
        with open(fileName, 'wb') as pickleFile:
            pickle.dump(state, pickleFile)

    @classmethod
    def maxID(cls):
        if len(cls.allEmployees) == 0:
            maxi = 0
        else:
            maxi = cls.allEmployees[0].id
        for emp in cls.allEmployees:
            if emp.id > maxi:
                maxi = emp.id
        return maxi



# Employee("ahmed ali",2000,'finance')
# Employee("salma ahmed",3000,'HR')
# Employee("amr ahmed",4000,'Eng')
# Employee("ali mahmoud",5000,'HR')


while True:
    os.system('cls')
    print()
    print("0-import csv or pickle")
    print("1-new")
    print("2-search")
    print("3-delete")
    print("4-show all")
    print("5-export")
    print("6-export department")
    print("7-export pickle")
    print("8-quit")

    print()
    process = input("Choose process: ")
    match process:
        case '0':
            print("1-CSV\n2-Pickle")
            method = input("Choose Method: ")
            match method:
                case '1':
                    Employee.csvImport("emps_in.csv")
                case '2':
                    Employee.importPickle("emps.pkl")

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
            # delete
        case '4':
            Employee.showMethod()
            # show all
        case '5':
            Employee.exportEmployees("emps_out.txt")
        case '6':
            depDict = Employee.makeDeparttmentDict()
            Employee.exportDepartment(depDict, "deps.txt")
        case '7':
            Employee.exportPickle("emps.pkl")
        case '8':
            print("bye")
            break
        case _:
            print("invalid process number")
    input("...")





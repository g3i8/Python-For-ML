import os
import csv
import pickle

id_list = []
idCount = 0
name_list = []
sal_list = []
dep_list = []
welcomeList = ["import csv or pickle","new", "search", "delete", "show all","export","export department", "export pickle", "exit"]
importList = ["csv", "pickle"]

def csvImport(fileName):
    with open(fileName, mode='r') as file:
        file.readline()
        csvFile = csv.reader(file)
        for line in csvFile:
            #continue
            addFun(line)

def showMenu(List):
    for (index, word) in enumerate(List):
        print(f'{index}-{word}')
    choice = input("enter choice:")
    return choice

def printFunc(index):
    print(f'id= {id_list[index]}, Name= {name_list[index]}, salary= {sal_list[index]}, dep= {dep_list[index]}')

def checkFunc(searchValue):
    returnList=[]
    for (index, name) in enumerate(name_list):
        if name.strip().lower().startswith(searchValue):
            returnList.append(index)
        else:
            returnList.append(-1)
    return returnList


def addFun(info):
    global idCount
    splitedInfo = info
    if len(splitedInfo) < 3:
        print("invalid entry!")
    else:
        if(idCount<1):
            idCount=1
        else:
            idCount +=1
        name_list.append(splitedInfo[0])
        id_list.append(idCount)
        if splitedInfo[1] == '' or not (splitedInfo[1].isnumeric()):
            salary = 0.0
            sal_list.append(salary)
        else:
            salary = float(splitedInfo[1])
            sal_list.append(salary)
        dep_list.append(splitedInfo[2])
        print("added new employee:")
        print(f'id= {idCount}, Name= {splitedInfo[0]}, salary= {salary}, dep= {splitedInfo[2]}')
def searchFunc():
    indexList = checkFunc(searchValue)
    for index in indexList:
        if(index>-1):
            printFunc(index)

def deleteFunc(deleteValue):
    indexList = checkFunc(deleteValue)
    index=0
    while index < len(indexList):
        if (indexList[index] == -1):
            index = index + 1
        else:
            print("deleting employee:")
            printFunc(index)
            indexList.remove(indexList[index])
            name_list.remove(name_list[index])
            dep_list.remove(dep_list[index])
            sal_list.remove(sal_list[index])
            id_list.remove(id_list[index])

def showAllFunc():
    index=0
    if(not name_list):
        print("nothing to show")
    else:
        while(index < len(id_list)):
            printFunc(index)
            index+=1

while 1:
    input()
    os.system('cls')
    process = showMenu(welcomeList)
    match process:
        case '0':
            uploadChoice = showMenu(importList)
            match uploadChoice:
                case '0':
                    csvImport('emps_in.csv')
                case '1':
                    #state={}
                    try:
                        with (open("emp.pkl", "rb")) as pickleFile:
                            restoredState=pickle.load(pickleFile)
                            for key, value in restoredState.items():
                                id_list.append(key)
                                name_list.append(value[0])
                                sal_list.append(value[1])
                                dep_list.append(value[2])
                    except:
                        print("pickle file doesn't exist")
                case _:
                    print("invalid choice")
        case '1':
            information = input("enter name, salary, dep:").split(',')
            splitedInformation=list(map(str.strip, information))
            addFun(splitedInformation)

        case '2':
            searchValue = input("search by first name:").strip()
            searchFunc()
        case '3':
            deleteValue = input("delete by first name:").strip()
            deleteFunc(deleteValue)
        case '4':
            showAllFunc()
        case '5':
            with open("emp.txt", 'w') as file:
                index=0
                while (index < len(id_list)):
                    file.write(f"id= {id_list[index]}, Name= {name_list[index]}, salary= {sal_list[index]}, dep= {dep_list[index]}\n")
                    index += 1
        case '6':
            depDic={}
            depDic = {dep: [] for dep in dep_list}
            for index,dep in enumerate(dep_list):
                #depDic[dep]=[]
                depDic[dep].append((id_list[index], name_list[index], sal_list[index]))
            with open("dep.txt", 'w') as file:
                for key,value in depDic.items():
                    file.write(f"{key}\n")
                    for val in value:
                        file.write(f"id= {val[0]}, Name= {val[1]}, salary= {val[2]}\n")
        case '7':
            state={}
            #state = {id: () for id in id_list}
            for index, id in enumerate(id_list):
                state[id]=(name_list[index], sal_list[index], dep_list[index])
            with open("emp.pkl",'wb')as pickleFile:
                pickle.dump(state,pickleFile)
        case '8':
            print("bye")
            break
        case _:
            print("invalid choice")

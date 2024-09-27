
import os

id_list = [1, 2, 3, 4]
idCount = 4
name_list = ["ahmed ali", "salma ahmed", 'amr ahmed', 'ali mahmoud']
sal_list = [2000, 3000, 4000, 5000]
dep_list = ['finance', 'HR', 'Eng', 'HR']
welcomeList = ["new", "search", "delete", "show all", "exit"]
while 1:
    input()
    os.system('cls')
    for (index, word) in enumerate(welcomeList):
        print(f'{index+1}-{word}')
    process = input("enter process:")
    match process:
        case '1':
            info = input("enter name, salary, dep:")
            splitedInfo = info.replace(" ", "").split(',')
            # print(splitedInfo)
            if len(splitedInfo) < 3:
                print("invalid entry!")
            else:
                name_list.append(splitedInfo[0])
                idCount = idCount + 1
                id_list.append(idCount)
                if splitedInfo[1] == '' or not(splitedInfo[1].isnumeric()):
                    salary = 0.0
                    sal_list.append(salary)
                else:
                    salary = float(splitedInfo[1])
                    sal_list.append(salary)
                # print(sal_list)
                dep_list.append(splitedInfo[2])
                # print(dep_list)
                print("added new employee:")
                print(f'id= {idCount}, Name= {splitedInfo[0]}, salary= {salary}, dep= {splitedInfo[2]}')
        case '2':
            searchValue = input("search by first name:").strip()
            for (index, name) in enumerate(name_list):
                # print(name.strip().lower() , searchValue.lower())
                if searchValue and name.strip().lower().startswith(searchValue):
                    print(f'id= {id_list[index]}, Name= {name_list[index]}, salary= {sal_list[index]}, dep= {dep_list[index]}')
        case '3':
            deleteValue = input("delete by first name:").strip()
            #for (index, name) in enumerate(name_list):
            index = 0
            while index < len(name_list):
                if name_list[index].strip().lower().startswith(deleteValue):
                    print("deleting employee:")
                    print(f'id= {id_list[index]}, Name= {name_list[index]}, salary= {sal_list[index]}, dep= {dep_list[index]}')
                    # name_list[index] = ""
                    # dep_list[index] = ""
                    # sal_list[index] = 0.0
                    name_list.remove(name_list[index])
                    dep_list.remove(dep_list[index])
                    sal_list.remove(sal_list[index])
                    id_list.remove(id_list[index])
                    # idCount = idCount - 1
                else:
                    index = index + 1
        case '4':
            for (index, id) in enumerate(id_list):
                print(f'id= {id}, Name= {name_list[index]}, salary= {sal_list[index]}, dep= {dep_list[index]}')
        case '5':
            print("bye")
            break
        case _:
            print("invalid process")

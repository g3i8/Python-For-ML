# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

balance=25000
pin=1234
print("welcome to our bank")
pinInput=int(input("enter your 4 digits pin number:"))
while 1:
    if pinInput==pin:
        print()
        print()
        print("1-withdraw")
        print("2-Balance Inquiry")
        print("3-Fast cash")
        print("3-exit")
        print()
        print()
        process=int(input("choose process:"))
        if process>4 or process<1:
            print("invalid process")
            break;
        else:
            match process:
                case 1:
                    withdrawAmount=int(input("enter withdraw amount multiple of (100):"))
                    if ((withdrawAmount % 100)==0) and withdrawAmount<balance:
                        balance=balance-withdrawAmount
                        print()
                        print("successful withdraw")
                        print("remaining balance:",balance)
                        break
                    else:
                        print("invalid withdrawal!")
                case 2:
                    print("your balance=",balance)
                case 3:
                    print("1-500")
                    print("2-1000")
                    print("3-5000")
                    print("4-10000")
                    print("5-50000")
                    print()
                    fastAmount=int(input("choose amount:"))
                    if fastAmount>5 or fastAmount<1:
                        print("invalid or insufficient balance!")
                    else:
                        match fastAmount:
                            case 1:
                                if balance<500:
                                    print("invalid or insufficient balance!")
                                else:
                                    balance = balance - 500
                                    print("successful withdraw")
                                    print("remaining balance:", balance)
                                    break
                            case 2:
                                if balance < 1000:
                                    print("invalid or insufficient balance!")
                                else:
                                    balance = balance - 1000
                                    print("successful withdraw")
                                    print("remaining balance:", balance)
                                    break
                            case 3:
                                if balance < 5000:
                                    print("invalid or insufficient balance!")
                                else:
                                    balance = balance - 5000
                                    print("successful withdraw")
                                    print("remaining balance:", balance)
                                    break
                            case 4:
                                if balance < 10000:
                                    print("invalid or insufficient balance!")
                                else:
                                    balance = balance - 10000
                                    print("successful withdraw")
                                    print("remaining balance:", balance)
                                    break
                            case 5:
                                if balance < 50000:
                                    print("invalid or insufficient balance!")
                                else:
                                    balance = balance - 50000
                                    print("successful withdraw")
                                    print("remaining balance:", balance)
                                    break
                case 4:
                    print("bye bye")
                    break;
    else:
        print("wrong pin")
        break;





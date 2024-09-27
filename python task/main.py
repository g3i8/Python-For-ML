# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywherfor classes, files, tool windowse , actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('dody')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# hours=input("enter hours:")
# rate=input("enter rate:")
# pay=float(hours)* float(rate)
# print("pay:",pay)

# x=5
# if x<10:
#     print("smaller")
# if x>20:
#     print("bigger")
#
# print("finish")

# score=int(input("enter your score"))
#
# if score<60:
#     print("your grade:F")
# elif score<65:
#     print("your grade:D")
# elif score<75:
#     print("your grade:C")
# elif score<85:
#     print("your grade:B")
# else:
#     print("your grade:A")

hours=input("enter hours:")
rate=input("enter rate:")
if float(hours)>40:
    pay = 40 * float(rate)+(float(hours)-40)*1.5*float(rate)
else:
    pay=float(rate)*float(hours)
print("pay:",pay)



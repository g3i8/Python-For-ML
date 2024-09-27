import random
import os

tries = 6
historyList=[]
correctList=[]

def wordFunc():
    with open('words.txt', 'r') as file:
        data = file.read().splitlines()
        word = random.choice(data)
        return word

def letterFunc():
    while 1:
        try:
            letter = input("enter a letter:").lower().strip()
            if len(letter) > 1:
                letter = letter[0]
            if letter == '':
                continue
            elif letter in historyList:
                print("letter was entered before")
            else:
                historyList.append(letter)
                return letter
        except:
            print("error")
            break

checkFunc=lambda letter,word:letter in word
# print(checkFunc('m',"sara"))

def hideFunc(word,correctList):
    hiddenWord=[]
    for i in range(len(word)):
        hiddenWord.append('_')
    for index,letter in enumerate(word):
        if letter in correctList:
            hiddenWord[index]=letter
    print(*hiddenWord)

#hideFunc("dode",[])

puzzleWord = wordFunc()
print(puzzleWord)
while 1:
    print(len(correctList))
    print(len(puzzleWord))

    input()
    os.system('cls')

    #show logic
    print("tries = ",tries)
    hideFunc(puzzleWord, correctList)
    puzzleLetter = letterFunc()

    #progress logic
    if checkFunc(puzzleLetter,puzzleWord):
        print("correct letter")
        correctList.append(puzzleLetter)
        #hideFunc(puzzleWord, correctList)
    else:
        print("incorrect letter")
        tries-=1


    # exiting logic
    if tries < 1 or len(correctList) == len(set(puzzleWord)):

        os.system('cls')
        print("tries = ", tries)
        hideFunc(puzzleWord, correctList)

        if len(correctList) < len(set(puzzleWord)):
            result = "you lost"
        else:
            result = "you won"
        print("game over,", result)
        break


# l=letterFunc()
# print(l)










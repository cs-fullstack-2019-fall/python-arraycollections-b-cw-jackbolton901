# Main function
def main():
    problem1()
    problem2()
    problem5()

def problem1():
    arrayForProblem1 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem1[2])
    print(len(arrayForProblem1))
    arrayForProblem1.pop(1)
    print(arrayForProblem1[2])
def problem2():
    userIn = ""
    while userIn != "q":
        userIn = input("enter something or press q to quit.   ")
# Skipping problem 3... 4 is under the called main function
def problem5():
    myArray = [38, 44, 47, 40, 9, 22, 50]
    userNum = int(input("enter a number  "))
    hiCount = 0
    loCount = 0
    eqCount = 0
    for v in myArray:
        if userNum > v:
            hiCount = hiCount + 1
        elif userNum < v:
            loCount = loCount + 1
        else:
            eqCount = eqCount + 1
        # !! : you are printing for every iteration AND you should have some string formatting to say what each print line is for f'{hiCount} numbers are higher than {userNum}'    
        print(hiCount) 
        print(loCount)
        print(eqCount)


# the main function will run problems 1, 2, and 5
main()

# problem 4
theArray = [11, 13, 23, 24, 50]
for x in theArray:
    theArray.reverse() # !! : DO NOT USE A FUNCTION
print(theArray)
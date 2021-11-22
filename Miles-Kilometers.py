'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 
#       A quick application that converts 
#       values between different unit conversions
#
#   Only doing between miles and kilometers for this application
#
#   Uses the Fibonacci sequence to do the calculations
#
#   https://www.geeksforgeeks.org/top-12-data-structure-algorithms-to-implement-in-practical-applications-in-2021/
#
#   Consider the sequence 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …
#   In the above example, you can take two consecutive numbers 8 and 13.  
#   The smaller number is in miles i.e 8 and the bigger one is in kilometers i.e. 13.
#
#   8 in miles = 13 in kilometers.
#
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Terrible code to calculate fibonacci sequence
'''
def fibonacci():
    fib1 = 0
    fib2 = 1
    print(fib1)
    print(fib2)
    for x in range(30):
        fibtemp = fib1 + fib2
        fib1 = fib2
        fib2 = fibtemp
        print(fibtemp)
'''
Calculates the next value in the fibonacci sequence
'''
def finalFibonacci(minus1, minus2):
    return int(minus1 + minus2)

def printFibonacci(minus2, minus1):
    print(minus2, "miles to ", minus1, " kilometers")

'''
Main Function
'''
def main():
    print("Hello")
    # fibonacci()           #   Test code for fibonacci sequence

    # User Input Here
    while True:
        print("\t 1. Miles")
        print("\t 2. Kilometers")
        originalTemp = input("Please enter the original unit:\t")
        if originalTemp == "Miles" or originalTemp == "miles" or originalTemp == "MILES" or originalTemp == "mi" or originalTemp == "Mi" or originalTemp == "MI" or originalTemp == int(1):
            originalUnitInput = "miles"
            break
        if originalTemp == "Kilometers" or originalTemp == "kilometers" or originalTemp == "KILOMETERS" or originalTemp == "km" or originalTemp == "Km" or originalTemp == "KM" or originalTemp == int(1):
            originalUnitInput = "kilometers"
            break
        else:
            print("Input not chosen correctly")


    while True:
        originalUnitValue = int(input("Please enter the value to be converted:\t"))
        if (isinstance(originalUnitValue, int)) == True:
            break
        else: print("Please enter a valid integer")

    while True:
        print("\t 1. Miles")
        print("\t 2. Kilometers")
        newUnitTemp = input("Please enter the original unit:\t")
        if newUnitTemp == "Miles" or newUnitTemp == "miles" or newUnitTemp == "MILES" or newUnitTemp == "mi" or newUnitTemp == "Mi" or newUnitTemp == "MI" or newUnitTemp == int(1):
            newUnitInput = "miles"
            break
        if newUnitTemp == "Kilometers" or newUnitTemp == "kilometers" or newUnitTemp == "KILOMETERS" or newUnitTemp == "km" or newUnitTemp == "Km" or newUnitTemp == "KM" or newUnitTemp == int(1):
            newUnitInput = "kilometers"
            break
        else:
            print("Input not chosen correctly")

    print("\n", originalUnitValue, "\t",originalUnitInput, "\t will be converted to \t", newUnitInput, "\n")

    # Fibonacci Stuff here
    fibonacciArr = [0, 1]           # List that stores the fibonacci sequence. 

    while True:
        tempFibonacci = finalFibonacci(fibonacciArr[-1], fibonacciArr[-2])
        fibonacciArr.append(tempFibonacci)
        if fibonacciArr[-1] <= originalUnitValue:
            break

    if newUnitInput == originalUnitInput: print("Converting between the same units!")
    elif originalUnitInput == "miles":
        printFibonacci(fibonacciArr[-2], fibonacciArr[-1])
    elif originalUnitInput == "kilometers":
        printFibonacci(fibonacciArr[-1], finalFibonacci(fibonacciArr[-2], fibonacciArr[-1]))
    else: print("IDK")



if __name__ == "__main__":
    main()
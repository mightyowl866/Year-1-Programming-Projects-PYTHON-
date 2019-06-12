def factorial(num):
        if num == 0:
            return 1
    #0! always equals 1
        else:
            return num * factorial(num-1)

    #The input is subtracted for every calculation.
    # Example: 5! = 5x4x3x2x1

num = int(input("Please enter number: "))

#The input

print("The factorial is: " , factorial(num))
#Results

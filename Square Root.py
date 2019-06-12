def square_root(num):
    guess = num/2
    while (guess * guess - num) > 0.0001:
        print(guess)
        guess= (guess + num/guess)/2
    return guess
#Function for squareroots.

guess=int(input("Please enter a number: "))

print(square_root(guess))
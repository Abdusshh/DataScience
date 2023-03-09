import sys

#write a function that takes a list of numbers and returns a list of odd numbers
def findOddNumbers(numbers):
    oddNumbers = []
    for number in numbers:
        if number % 2 != 0:
            oddNumbers.append(number)
    return oddNumbers
#write a function that takes a list of numbers and returns a list of odd numbers in least space possible
def findOddNumbers2(numbers):                                 
    return [number for number in numbers if number % 2 != 0]

#write a function that genereates random reference codes
import random
def generateReferenceCode():
    referenceCode = ""
    for i in range(0, 10):
        referenceCode += str(random.randint(0, 9))
    return referenceCode

print(generateReferenceCode())

#Write a program that takes an input and returns the input in reverse
def reverseInput():
    userInput = input("Enter a string to reverse: ")
    return userInput[::-1]

# x = int(input())
# print(x)

print("%.150f" % 0.2)

def tryExcept():
    try:
        x = int(input("Enter a number: "))
        print(x)
    except ValueError:
        print("That's not a number!")
        tryExcept()

# tryExcept()

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                if len(stack) == 0:
                    return False
                if stack[-1] != "(":
                    return False
                stack = stack[:-1]
            elif s[i] == "]":
                if len(stack) == 0:
                    return False
                if stack[-1] != "[":
                    return False
                stack = stack[:-1]
            elif s[i] == "}":
                if len(stack) == 0:
                    return False
                if stack[-1] != "{":
                    return False
                stack = stack[:-1]
            else:
                stack.append(s[i])
        if len(stack) > 0:
            return False
        return True
    
#Override len function
# def len(x):
#     return 50

# print(len("abc")*2)

#Write a function called main that takes an integer system argument and creates the multiplication table for that number
def main():
    number = int(sys.argv[1])
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

main()


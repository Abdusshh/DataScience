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

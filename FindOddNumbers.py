#write a function that takes a list of numbers and returns a list of odd numbers
def findOddNumbers(numbers):
    oddNumbers = []
    for number in numbers:
        if number % 2 != 0:
            oddNumbers.append(number)
    return oddNumbers
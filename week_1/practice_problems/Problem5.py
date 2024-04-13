def listManipulation(inputList):
    even_numbers = [num for num in inputList if num % 2 == 0]
    doubled_numbers = [num * 2 for num in even_numbers]    
    total_sum = sum(doubled_numbers)
    
    return total_sum

print(listManipulation([1, 2, 3, 4, 5]))
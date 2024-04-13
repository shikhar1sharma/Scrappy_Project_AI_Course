def addNNumbers(*args): # we can pass any number of arguments in args
    sum = 0;
    for arg in args:
        sum += arg;
    return sum

print (addNNumbers(2, 4, 4))
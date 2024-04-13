def temperatureConverter(temp, scale):
    if scale is 'C':
        return (temp * 9/5) + 32
    else:
        return (temp - 32) * 5/9
    

print(temperatureConverter(100, 'C'))
print(temperatureConverter(100, 'F'))
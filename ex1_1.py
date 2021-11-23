temp = input('Please input a temperature in degree Celsius:')
temp = float(temp)
if temp < 0:
    print('Freezing')
elif 0 <= temp and temp < 10:
    print('Very cold')
elif 10 <= temp and temp < 20:
    print('Cold')
elif 20 <= temp and temp < 30:
    print('Normal')
elif 30 <= temp and temp <40:
    print('Hot')
elif 40 < temp:
    print('Very hot')

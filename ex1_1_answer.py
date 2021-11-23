print('Temperature to Perceived Temperature Converter (0.1)')

temp = input('What temperature is outside? ')	# This returns a string
temp = float(temp) 			                    # This converts it to a float

perceived_temp = ''
if temp < 0:
    perceived_temp = 'freezing'
elif temp < 10:
    perceived_temp = 'very cold'
elif temp < 20:
    perceived_temp = 'cold'
elif temp < 30:
    perceived_temp = 'normal'
elif temp < 40:
    perceived_temp = 'hot'
else:
    perceived_temp = 'very hot'

print('Your temperature today is', perceived_temp)

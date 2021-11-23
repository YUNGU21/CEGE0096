print('Angles Checkers for Triangles (0.1) ')

angle1 = float(input('1st angle: '))
angle2 = float(input('2nd angle: '))
angle3 = float(input('3rd angle: '))

if angle1 + angle2 + angle3 != 180:
    print("You can't build any triangle out of these angles!!!")
elif angle1 == angle2 and angle2 == angle3:
    print('You can build an equilateral triangle')
elif angle1 == angle2 or angle2 == angle3 or angle3 == angle1:
    print('You can build an isosceles triangle')
else:
    print('You can build a scalene triangle')

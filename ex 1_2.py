angle_1 = input('Please input the 1st angle:')
angle_2 = input('Please input the 2nd angle:')
angle_3 = input('Please input the 3rd angle:')
angle_1 = float(angle_1)
angle_2 = float(angle_2)
angle_3 = float(angle_3)
if angle_1 + angle_2 + angle_3 != 180:
    print('not a triangle')
else:
    if angle_1 == angle_2 == angle_3:
        print('Equilateral triangle')
    elif angle_1 == angle_2 or angle_1 == angle_3 or angle_2 == angle_3:
        print('Isosceles triangle')
    else:
        print('Scalene triangle')
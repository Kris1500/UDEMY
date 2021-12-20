import calc_func
x = 0
try:
    x = int(input('Choose: 1-square, 2-rectangle, 3-triangle, 4-circle   '))
except:
    print('Invalid data')

if x == 1:
    calc_func.square_area()
if x == 2:
    calc_func.rectangle_area()
if x == 3:
    calc_func.square_triangle()
if x == 4:
    calc_func.square_circle()
else:
    print('Choose: 1-square, 2-rectangle, 3-triangle, 4-circle')

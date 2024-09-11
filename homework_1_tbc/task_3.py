#3
side1 = input('enter first side: ')
side2 = input('enter second side: ')
base = input('enter base: ')
height = input('enter height: ')

Triangle_Perimeter = int(side1) + int(side2) + int(base)
Triangle_Area = (int(base) * int(height))/2

print(Triangle_Perimeter)
print(Triangle_Area)
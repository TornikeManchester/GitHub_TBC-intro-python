#3
side1 = input('enter first side: ')
side2 = input('enter second side: ')
base = input('enter base: ')
height = input('enter height: ')

triangle_perimeter = int(side1) + int(side2) + int(base)
triangle_area = (int(base) * int(height))/2

print(triangle_perimeter)
print(triangle_area)
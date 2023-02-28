pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

#math2

base1 = float(input('the First Base of a Trapezoid: '))
base2 = float(input('the Second Base of a Trapezoid: '))
height = float(input('the Height of a Trapezoid: '))

Area = 0.5 * (base1 + base2) * height

Median = 0.5 * (base1+ base2)

print("\n Area of a Trapezium = %.2f " %Area)
print(" Median of a Trapezium = %.2f " %Median)


#math3

from math import tan, pi
n_sides = int(input("number of sides: "))
s_length = float(input("length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)


#math4

base = float(input('Length of base: '))
h = float(input('Measurement of height: '))
area = base * h
print("Area is: ", area)
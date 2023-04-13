# Name: Seoyeon Jo
# SBUID: 115935813
##################### SCORE ######################
#######  Score:  3/10
#################################################
# Remove the ellipses (...) when writing your solutions.

# your output
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/seoyeonjo23/Homework_1.py"
# Wear Scarf -- wrong
# The area of the triangle is : 32.0 - correct, its perimeter is : 84.0-- wrong
# The area of the polygon is : 2.580488365589943-- wrong
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit):
    celsius = float(5 / 9 * (int(fahrenheit) - 32))
    return celsius

def what_to_wear(celsius):
   if celsius < -10:
       print('Wear Puffy jacket')
   elif celsius >= -10 or celsius < 0:
       print('Wear Scarf')
   elif celsius == 0:
       print('Wear Scarf or Sweater')
   elif celsius > 0 or celsius < 10:
       print('Wear Sweater')
   elif celsius == 10:
       print('Wear Sweater or Ligh jacket')
   elif celsius > 10 or celsius < 20:
       print('Wear Light jacket')
   elif celsius == 20:
       print('Wear Light jacket or T-shirt')
   elif celsius > 20:
       print('Wear T-shirt')
    
# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    A = abs(((x1 * y2 + x2 * y3 + x3 * y1) - (x1 * y3 + x2 * y1 + x3 * y2)) / 2)
    return A
    
def euclidean_distance(x1, y1, x2, y2):
    dist = ((x1 - x2)**2 + (y1 + y2)**2) * 0.5
    return dist    
    
def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    s1 = euclidean_distance(x1, y1, x2, y2)
    s2 = euclidean_distance(x2, y2, x3, y3)
    s3 = euclidean_distance(x3, y3, x1, y1)
    
    P = s1 + s2 + s3
    return P

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


def deg2rad(deg):
    import math
    rad = deg * math.pi / 180
    return rad
    
def apothem(number_sides, length_side):
    import math
    apo = length_side / (2 * math.tan(180 / number_sides))
    return apo

def polygon_area(number_sides, length_side):
   area = (number_sides * length_side * apothem(number_sides, length_side)) / 2
   return area


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))


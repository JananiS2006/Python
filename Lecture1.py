# Types of scalar objects
type(7)
<class 'int'>
type(3.0)
<class 'float'>
type(True)
<class 'bool'>
type(False)
<class 'bool'>
type(1234)
<class 'int'>
type(8.99)
<class 'float'>
type(9.0)
<class 'float'>
type(True)
<class 'bool'>
type(False)
<class 'bool'>
# Type Casting (Convert one type to another)
float(3)
#ans - 3.0
int(5.2)
#ans - 5
int(5.9)
#ans - 5
round(5.9)
#ans - 6
float(123)
#ans - 123.0
round(7.9)
#ans - 8
float(round(7.2))
#ans - 7.0
int(7.2)
#ans - 7
int(7.9)
#ans- 7
# Expression
3 + 2 #5
(4 + 2) * 6 - 1 #35
type((4 + 2) * 6 - 1) #int
float((4 + 2) * 6 - 1) #35.0
(13 - 4) / (12 * 12) #0.0625
type(4 * 3) #int
type(4.0 * 3)#float
int(1 / 2)#0
5 / 3#1.6666
5 // 3 #1
5 % 3 #2

# Which of these are allowed in Python?
# Assignment - (variable = value)
x = 6
6 = x  # SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
x * y = 3 + 4  # SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
xy = 3 + 4
xy
xy + 1

a = 355 / 133 * (2.2 * 2)
c = 355 / 133 * (2.2 * 2)
# Best code style
pi = 355 / 113
radius = 2.2
area = pi * (radius ** 2)
circumference = pi * (radius * 2)

# Instead of reusing
a = c

# Executed in order - what are the values of meters and feet variables at each line in the code
meters = 100
feet = 3.2802 * meters
meters = 200
feet
meters

# Swap values of x and y 
x = 1
y = 2
y = x
x = y
# Using temp
x = 1
y = 2
temp = y
y = x
x = temp
x #2
y #1
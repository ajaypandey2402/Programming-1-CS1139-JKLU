'''
#1 
#Write a program that prompts the user to enter the centre of a circle (x1, y1), its radius r, and a
#second point (x2, y2), and displays whether the second point lies inside, on the boundary of, or
#outside the circle. The formula for computing the distance between two points is
#distance = √[(x2 – x1)^2 + (y2 – y1)^2]

x1 = int(input('Enter X1: '))
y1 = int(input('Enter Y1: '))
r = int(input('Enter radius r: '))
x2 = int(input('Enter X2: '))
y2 = int(input('Enter Y2: '))
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
if distance > r:
    print('Outside the circle')
elif distance == r:
    print('On the boundary')
else:
    print('inside the circle')
'''
'''
#2 
#Write a program that prompts the user to enter the side of a regular pentagon and displays its area.
#The formula for computing the area of a pentagon is Area = (5 * s^2) / (4 * tan(π / 5)), where s is the
#length of a side.

s = int(input('Enter the side of a regular pentagon: '))
area = (5*s**2)/(4*0.7265)
print('The area is:', round(area, 2))
'''
'''
#3
#Take 3 angles as input, and find whether they can form the angles of a triangle or not. If they can,
#further classify the triangle as acute-angled, right-angled or obtuse-angled. Consider invalid cases
#also.

a = int(input('Input the 1st angle: '))
b = int(input('Input the 2nd angle: '))
c = int(input('Input the 3rd angle: '))
if (a + b + c) == 180:
    if (a<90) and (b<90) and (c<90):
        print('This is an acute-angled triangle')
    elif (a==90) or (b==90) or (c==90):
        print('This is a right-angled triangle')
    else:
        print('This is an obtuse-angled triangle')
else:
    print('Does not form a triangle')
'''
'''
#4
#Take a 4 digit number as input and find the sum of its first two digits and the sum of its last two
#digits separately. Also, check if the two sums are equal or not.

n = int(input('Enter a 4-digit number: '))
d1 = n//1000
d2 = (n//100)%10
d3 = (n//10)%10
d4 = n%10
sum1 = d1 + d2
sum2 = d3 + d4
if sum1 == sum2:
    print(sum1, sum2, 'The sums are equal')
else:
    print(sum1, sum2, 'The sums are not equal')
'''    
'''
#5
#Take a 5 digit number as input and print the largest digit of the number. Do not use any in-built
#functions and do not use loops. Also print the position of that digit counted from the left. If the
#largest digit occurs more than once, print the position of its first occurrence.

n = int(input('Enter a 5-digit number: '))
d1 = n//10000
d2 = (n//1000)%10
d3 = (n//100)%10
d4 = (n//10)%10
d5 = n%10
if (d1 >= d2) and (d1 >= d3) and (d1 >= d4) and (d1 >= d5):
    print('The largest digit is ', d1, '. The position is 1', sep='')
elif (d2 >= d3) and (d2 >= d4) and (d2 >= d5):
    print('The largest digit is ', d2, '. The position is 2', sep='')
elif (d3 >= d4) and (d3 >= d5):
    print('The largest digit is ', d3, '. The position is 3', sep='')
elif (d4 >= d5):
    print('The largest digit is ', d4, '. The position is 4', sep='')
else:
    print('The largest digit is ', d5, '. The position is 5', sep='')
'''
'''
#6
#Rotate the values of three integer variables cyclically, so that the value of a moves to b, the value of
#b moves to c, and the value of c moves to a, without using a fourth variable or multiple
#assignment operation.

a = int(input('Enter the 1st variable: '))
b = int(input('Enter the 2nd variable: '))
c = int(input('Enter the 3rd variable: '))
a = a + b + c 
c = a - b - c
a = a - b - c
print(a, b, c)
'''
'''
#7
#Take a 3 digit number as input. Check if it is a Harshad number or not, i.e. whether the number is
#exactly divisible by the sum of its digits. E.g. 1 + 5 + 3 = 9 and 153 / 9 = 17, so 153 is a Harshad
#number.

n = int(input('Enter a 3-digit number: '))
d1 = n//100
d2 = (n//10)%10
d3 = n%10
if n%(d1+d2+d3) == 0:
    print('It is a Harshad number')
else:
    print('It is not a Harshad number')
'''


'''
#1
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
s = int(input('Enter the side of a regular pentagon: '))
area = (5*s**2)/(4*0.7265)
print('The area is:', round(area, 2))
'''
'''
#3
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
n = int(input('Enter a 3-digit number: '))
d1 = n//100
d2 = (n//10)%10
d3 = n%10
if n%(d1+d2+d3) == 0:
    print('It is a Harshad number')
else:
    print('It is not a Harshad number')
'''


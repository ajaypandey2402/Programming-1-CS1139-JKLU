'''
#8
v = int(input('Enter the initial quantity of water: '))
n = int(input('Enter the number of days: '))
if (v>0) and (n>0):
    final_quantity = 200 + (v - 200) * (0.95)**n
    print('The final quantity of water is', final_quantity)
else:
    print('Invalid input')
'''
'''
#9
coefficients = input('Enter coefficients a1, b1, c1, a2, b2, c2: ').split()
a1 = int(coefficients[0])
b1 = int(coefficients[1])
c1 = int(coefficients[2])
a2 = int(coefficients[3])
b2 = int(coefficients[4])
c2 = int(coefficients[5])
if (a1*b2 - a2*b1) != 0:
    x = (c1*b2 - c2*b1)/(a1*b2 - a2*b1)
    y = (a1*c2 - a2*c1)/(a1*b2 - a2*b1)
    print(f"The point of intersection is: {x:.2f}, {y:.2f}") 
else:
    print('Straight lines are parallel or identical')
'''
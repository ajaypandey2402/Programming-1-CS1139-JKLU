'''
#8
#Suppose a water tank initially holds V litres of water. Every day 5% of the water present in the tank
#evaporates, and then exactly 10 litres of fresh water is added to it. Therefore, the daily retention
#rate is 1 – 0.05 = 0.95. After the first day, the quantity in the tank becomes
#V * 0.95 + 10
#After the second day, the quantity in the tank becomes
#(V * 0.95 + 10) * 0.95 + 10
#After the third day, the quantity in the tank becomes
#((V * 0.95 + 10) * 0.95 + 10) * 0.95 + 10
#and so on.
#Write a program that prompts the user to enter the initial quantity of water and the number of
#days (N) and displays the quantity of water in the tank after the Nth day. Check for valid and
#invalid cases. Do not use loops.

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
#Enter the coefficients of two straight lines a1x + b1y = c1 and a2x + b2y = c2 and display their point
#of intersection. Handle all the cases for invalid input as well as the cases where the two lines are
#parallel or coincident, and display the solution till exactly 2 decimal places.

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

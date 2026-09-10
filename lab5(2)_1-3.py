#1
#Street Lamps on a Highway. The lamp posts on a highway are numbered from X to Y. 
#Every post whose number is divisible by N is out of order. 
#Display the numbers of the posts that are still working, along with how many of them there are. 
#Consider the posts numbered X ≤ i < Y.
'''
x = int(input('Enter X: '))
y = int(input('Enter Y: '))
n = int(input('Enter N: '))
count = 0
for i in range(x, y):
    if i%n != 0:
        print(i, end = ' ')
        count += 1
print()
print(count)
'''
#2
#Take a positive integer as input and display the product of its digits. 
#The number can be of any length.
'''
n = int(input('Enter a positive number: '))
prod = 1
while n > 0:
    prod *= n%10
    n = n // 10
print('The product of its digits is:', prod)
'''
#3
#Canteen Billing Counter. 
#The canteen cashier enters the amount of every bill of the day one by one. 
#To close the counter, the cashier enters -999. 
#A bill is called a large bill if its amount is greater than N, otherwise it is a small bill. 
#Count the large bills and the small bills of the day.
'''
n = int(input('Enter N: '))
count_small = 0
count_big = 0
bill = 0
while bill != -999:
    bill = int(input())
    if bill == -999:
        break
    elif bill > n:
        count_big += 1
    else:
        count_small += 1
print(count_big)
print(count_small)
'''
    


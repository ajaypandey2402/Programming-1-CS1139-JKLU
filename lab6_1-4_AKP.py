#1
#Display the following addition table:
'''
print(" "*14, 'Addition table')
print(" "*5, '1    2    3    4    5    6    7    8    9')
print('-'*47)
for i in range(1, 10):
    print(i, '|', end = '')
    for j in range(1, 10):
        if  i+j > 9:
            print(' '*1, i + j, end = ' ')
        else:
            print(' '*2, i + j, end = ' ')
    print()
'''
#2
#Parking Slot Allotment. A parking area has slots numbered from 1 to 1000. 
#Every slot whose number is divisible by N is reserved. However, 
#a reserved slot whose number is also divisible by 4 is kept for electric vehicle 
#charging and is not given to staff. Display the slot numbers given to the staff. 
#Use the continue statement with a while loop.
'''
n = int(input('Enter N: '))
slot = 0
print('The slot numbers given to the staff are: ')
while slot < 1000:
    slot += 1
    if slot%n == 0:
        if slot%4 == 0:
            continue
        print(slot, end = ' ')
'''
#3
#Display the following patterns for N lines (value of N taken from the user) using while loop:
'''
n = int(input('Enter N: '))
i = 1
print('a)')
while i <= n:
    for j in range(1, i+1):
        print(j, end = ' ')
    print()
    i += 1
print()
print('b)')
i = n
while i > 0:
    print('* '*i, end = ' ')
    print()
    i -= 1
print()
print('c)')
i = 1
while i <= n:
    print(' '*2*(n-i), '* '*i, sep = '', end = ' ')
    print()
    i += 1
'''
#4
#Take a positive integer as input from the user and display its octal equivalent 
#via the repeated division method. (without using any inbuilt function or format specifier). 
#The final result should be displayed as a string. 
#Check if the result matches the output of inbuilt oct() function.
'''
n = int(input('Enter N: '))
k = n
octal = ''
remainder = 0
sign = 1
if n == 0:
    print(n)
if n < 0:
    n = n*(-1)
    sign = -1
while n > 0:
    remainder = str(n%8)
    octal = remainder + octal
    n = n//8
octal = int(octal)

print('The octal equivalent is:', sign * octal)
print('Check:', oct(k))
'''
    

    
        
        
    


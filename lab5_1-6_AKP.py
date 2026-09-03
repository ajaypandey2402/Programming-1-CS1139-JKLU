'''
#1
#Take 2 numbers as input (X and Y) and a third number N. 
#Display all the numbers between X and Y
#(X < i <= Y) that are divisible by N.

x = int(input('Input the first number X: '))
y = int(input('Input the seconf number Y: '))
n = int(input('Input the third number N: '))
for i in range(x+1, y+1):
    if i%n == 0:
        print(i, 'is divisible by', n)
'''
'''
#2
#Take a positive integer as input and display the sum of its digits. 
#The number can be of any length.

n = int(input('Input a positive integer: '))
sum =  0
while n > 0:
    sum += n%10
    n = n//10
print('The sum of its digits is', sum)
'''
'''
#3
#Take a positive integer N as input followed by repeatedly taking numbers from the user till the time 
#user entered -999. At the end display the count of input numbers that are divisible by N and the 
#count of input numbers that are not divisible by N.

n = int(input('Input a positive integer N: '))
r = int(input('Input an integer (to stop - input "-999"): '))
count1 = 0
count2 = 0
while r != -999:
    if r%n == 0:
        count1 += 1
    else:
        count2 += 1
    r = int(input('Input a new integer: ')) 
print('The count of input integers, that are divisable by N, is:', count1)
print('The count of input integers, that are not divisable by N, is:', count2)
'''
'''
#4
#Take a positive integer N as input and find its Factorial using a while loop. 
#Handle invalid cases as well.

n = int(input('Input a positive integer: '))
f = 1
if n >= 1:
    while n >= 2:
        f *= n
        n -= 1
    print(f)
else:
    print('Invalid input')
'''
'''
#5
#Take a positive integer as input. It may be of any length. 
#Check if it is palindrome or not. Do not use any inbuilt reverse functions.

a = int(input('Enter a positive integer: '))
b = a
c = a
length = 0
while b > 0:
  b = b//10
  length += 1
while a > 0:
  b += (a%10)*10**(length - 1)
  a = a//10
  length -= 1
if c == b:
  print('It is a palindrome')
else:
  print('It is not a palindrome')
'''
'''
#6
#Display the first N terms of the Fibonacci sequence starting from 1. 
#1, 1, 2, 3, 5, ….. till N terms

n = int(input('Enter N: '))
f1 = 1 
f2 = 1
if n == 1:
    print(f1)
elif n == 2:
    print(f1)
    print(f2)
else:
    f3 = f1 + f2
    print(f1)
    print(f2)
    print(f3)
    for i in range(n - 3):
        f1 = f2
        f2 = f3
        f3 = f1 + f2
        print(f3)
'''





    
    


        

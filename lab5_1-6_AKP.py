'''
#1
x = int(input('Input the first number X: '))
y = int(input('Input the seconf number Y: '))
n = int(input('Input the third number N: '))
for i in range(x+1, y+1):
    if i%n == 0:
        print(i, 'is divisible by', n)
'''
'''
#2
n = int(input('Input a positive integer: '))
sum =  0
while n > 0:
    sum += n%10
    n = n//10
print('The sum of its digits is', sum)
'''
'''
#3
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





    
    


        
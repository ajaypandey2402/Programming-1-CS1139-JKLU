#8
'''
n = [int(x) for x in input('Enter list of integers: ').split()]
s = 0
p = 1
for i in n:
    s += i
print('The sum of the integers equals to:', s)
for i in n:
    p *= i
print('The product of the integers equals to:', p)
if len(n) == 1:
    print('The smallest elemet equals to', s[0])
else:
    min1 = n[0]
    for i in n:
        if i <= min1:
            min1 = i
    print('The smallest element equals to', min1)
'''
#9
'''
n1 = [int(x) for x in input('Enter list of integers: ').split()]
length = 0
for i in n1:
    length += 1
if length == 1:
    print(n1)
else:
    for i in range(length):
        min1 = i
        for j in range(i + 1, length):
            if n1[j] < n1[min1]:
                min1 = j
        n1[i], n1[min1] = n1[min1], n1[i]
print(n1)
'''
#10
'''
s = input('Enter a hyphen-separated sequence of words: ')
l = []
current = ''
for ch in s:
    if ch == '-':
        if current:
            l.append(current)
            current = ''
    else:
        current += ch
if current:
    l.append(current)
length = 0
for i in l:
    length += 1
if length == 1:
    print('The sorted hyphen-separated sequence of words is:', l[0])
else:
    for i in range(length):
        min1 = i
        for j in range(i + 1, length):
            if l[j] < l[min1]:
                min1 = j
        l[i], l[min1] = l[min1], l[i]
    sorted_sequence = ''
    for i in range(length):
        sorted_sequence += l[i]
        if i != length-1:
            sorted_sequence += '-'
    print('The sorted hyphen-separated sequence of words is:',sorted_sequence)
'''
#11
'''
s = input('Enter a paragraph: ')
digits = 0 #48 - 57
uppers = 0 #65 - 90
lowers = 0 #97 - 122
specials = 0
for i in s:
    if ord(i) >= 48 and ord(i) <= 57:
        digits += 1 
    elif ord(i) >= 65 and ord(i) <= 90:
        uppers += 1 
    elif ord(i) >= 97 and ord(i) <= 122:
        lowers += 1 
    else:
        specials += 1
print('The count of digits is:', digits)
print('The count of upper alphabets is:', uppers)
print('The count of lower alphabets is:', lowers)
print('The count of special characters is:', specials)
print('Check with inbuilt functions:')
digits = 0
uppers = 0
lowers = 0
specials = 0
for i in s:
    if i.isdigit():
        digits += 1 
    elif i.isupper():
        uppers += 1 
    elif i.islower():
        lowers += 1 
    else:
        specials += 1
print('The count of digits is:', digits)
print('The count of upper alphabets is:', uppers)
print('The count of lower alphabets is:', lowers)
print('The count of special characters is:', specials)
'''
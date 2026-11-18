'''
#1
#Read a list of integers and a value V. Convert the list into a tuple and print the tuple, its length,
#the number of times V occurs in it, and the index of the first occurrence of V.

l = input('Enter a space-separated sequence of integers: ').split()
n = int(input('Enter an integer: '))
l = [int(x) for x in l]
count = l.count(n)
t = tuple(l)
length = len(t)
first = t.index(n)
print('Tuple:', t)
print('Length:', length)
print(f'Count of {n}: {count}')
print(f'First index of {n}: {first}')
'''
'''
#2
#Write a function count_vowels(s) that returns the number of vowels in the string s. Read a
#string, call the function and print the result.

def count_vowels(s):
    count = 0
    for ch in s:
        if ch in ('aeuio'):
            count += 1
    print('Vowels:', count)
s = input('Enter a string: ')
count_vowels(s)
'''
'''
#3
#Each section at JKLU is electing a class representative. Every student writes one candidate's
#name, and all the votes are entered on a single line. Store the vote count of each candidate in
#a dictionary and print the results in the order the candidates first appear. The candidate with
#the most votes wins; if there is a tie, the candidate who appears first in the list wins.

l = input('Enter names: ').split()
d = {}
for name in l:
    if name in d:
        d[name] += 1
    else:
        d[name] = 1
for name, count in d.items():
    print(f"{name}: {count}")
count_max = -1
count = 0
winner = ''
for i in l:
    count = l.count(i)
    if count > count_max:
        count_max = count
        winner = i
print('Winner:', winner)
'''
'''
#4
#Read a word and build a dictionary that stores how many times each letter occurs in it. Print
#the dictionary.

s = input('Enter a word: ')
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
print(d)
'''
'''
#5
#Write a function simple_interest(p, r, t=1) that returns the simple interest p * r * t / 100. 
#Read p and r, then print the interest for the default time and for t = 3.

def simple_interest(p, r, t=1):
    return(p * r * t / 100)
p = int(input('Enter P: '))
r = int(input('Enter R: '))
t = 3
print('1 year:', simple_interest(p, r))
print(t, 'years:', simple_interest(p, r, 3))
'''
'''
#6
#A faculty member wants to convert marks into grades. Write a function get_grade(marks)
#that returns A for 80 or above, B for 60 to 79, C for 40 to 59 and F below 40. Read the
#students' names and marks, print each student's grade using the function, and finally print a
#dictionary showing how many students received each grade (grades in the order they first
#appear).

def get_grade(marks):
    if marks >= 80:
        return('A')
    elif marks >= 60:
        return('B')
    elif marks >= 40:
        return('C')
    else:
        return('F')
n = int(input('Enter a number of students: '))
d = {}
for i in range(n):
    s = input('Enter a name and a grade: ').split()
    name = s[0]
    grade = int(s[1])
    d[name] = get_grade(grade)
for name, grade in d.items():
    print(f'{name}: {grade}')
g = {}
for grade in d.values():
    if grade in g:
        g[grade] += 1
    else:
        g[grade] = 1
print('Grade count:')
print(g)
'''
'''
#7
#Read a tuple of integers and create a new tuple containing only its even numbers. 
#Print the new tuple.

t = tuple(int(x) for x in input('Enter a tuple of integers: ').split())
t2 = []
for i in t:
    if i % 2 == 0:
        t2.append(i)
t2 = tuple(t2)
print(t2)
'''
'''
#8
#Read N countries and their capitals and store them in a dictionary. Then read a country name
#and print its capital, or Not found if the country is not in the dictionary.

n = int(input('Enter a number of countries: '))
d = {}
for i in range(n):
    s = input('Enter a country and its capital: ').split()
    d[s[0]] = s[1]
c = input('Enter a country: ')
if c in d.keys():
    print(d[c])
else:
    print('Not found')
'''
'''
#9
#The campus stationery shop keeps its stock in a dictionary that maps each item to its quantity.
#During the day it records two kinds of transactions: SELL item qty reduces the stock, and
#ADD item qty increases it (adding the item if it is new). If a sale asks for more than the
#available quantity, the sale is skipped and Insufficient stock: item is printed. At the end
#of the day, print the stock of every item.

n = int(input('Enter a number of items: '))
d = {}
for i in range(n):
    l = input('Enter an item and its quantity: ').split()
    d[l[0]] = int(l[1])
q = int(input('Enter a number of transactions: '))
for i in range(q):
    s = input('Enter a transaction: ').split()
    if s[1] not in d:
        d[s[1]] = int(s[2])
    if s[0] == 'SELL':
        if d[s[1]] - int(s[2]) < 0:
            print('insufficient stock:', s[1])
        else:
            d[s[1]] -= int(s[2])
    else:
        d[s[1]] += int(s[2])
for item, amount in d.items():
    print(f'{item}: {amount}')
'''
'''
#10
#Write a function stats(nums) that returns a tuple containing the smallest number,
#the largest number and the average of the list nums. Read a list of integer, call
#the function and print the returned tuple

def stats(nums):
    smallest = nums[0]
    biggest = nums[0]
    count = 0
    s = 0
    average = 0
    for i in range(len(nums)):
        if smallest > nums[i]:
            smallest = nums[i]
        elif biggest < nums[i]:
            biggest = nums[i]
        count += 1
        s += nums[i]
    average = s/count
    l = [smallest, biggest, average]
    return tuple(l)

n = [int(x) for x in input('Enter the integers: ').split()]
print(stats(n))
'''
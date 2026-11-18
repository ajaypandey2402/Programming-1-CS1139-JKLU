'''
#1
#Read a line of space-separated integers and store the even and odd 
#numbers in two separate lists. Print both lists.

l = [int(x) for x in input('Enter a space-separated line of integers: ').split()]
l_even = []
l_odd = []
for i in l:
    if i%2 == 0:
        l_even.append(i)
    else:
        l_odd.append(i)
print('Even:', l_even)
print('Odd:', l_odd)
'''
'''
#2
#Read a sentence and build a list of all the words that have more than 3 letters,
#in the order they appear. Print the list.

s = input('Enter a sentence: ').split()
s_words = []
for i in s:
    if len(i) > 3:
        s_words.append(i)
print(s_words)
'''
'''
#3
#The JKLU inter-hostel cricket league keeps a ball-by-ball record of every innings as a single line.
#Each ball is recorded as the runs scored on it (0, 1, 2, 3, 4 or 6), or as W if a wicket fell (no runs
#on that ball). An over has 6 balls, and the last over may be incomplete. The scorer wants the
#total runs, the number of wickets, the number of boundaries (balls on which 4 or 6 was
#scored), and a list of runs scored in each over.

l = input('Enter the record: ').split()
total = 0
wickets = 0
bound = 0
runs = []
over = 0
for i in range(len(l)):
    if (i+1)%6 == 0 or i == len(l)-1:
        if l[i].isdigit():
            if int(l[i]) == 4 or int(l[i]) == 6:
                bound += 1
                over += int(l[i])
            else:
                over += int(l[i])
            total += int(l[i])
        else:
            wickets += 1
        runs.append(over)
        over = 0
    else:
        if l[i].isdigit():
            if int(l[i]) == 4 or int(l[i]) == 6:
                bound += 1
                over += int(l[i])
            else:
                over += int(l[i])
            total += int(l[i])
        else:
            wickets += 1
print('Total Runs:', total)
print('Wickets:', wickets)
print('Boundaries:', bound)
print('Runs per over:', runs)
'''
'''
#4
#Read a list of integers and print the largest and the smallest number in it,
#without using max() or min().

l = [int(x) for x in input('Enter a space-separated line of integers: ').split()]
largest = l[0]
smallest = l[0]
for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
    elif l[i] < smallest:
        smallest = l[i]
print('Largest:', largest)
print('Smallest:', smallest)
'''
'''
#5
#Read a sentence and print its longest word. If two words have the same length, 
#print the one that comes first.

s = input('Enter a sentence: ').split()
maxx = s[0]
for i in range(len(s)):
    if len(s[i]) > len(maxx):
        maxx = s[i]
print(maxx)
'''
'''
#6
#The campus canteen wants a quick billing program. The first line lists the items on the menu
#and the second line lists their prices in the same order. The third line lists the items a student
#ordered, and an item can appear more than once. Print one line for each item that was
#ordered, in menu order, showing the item, its quantity and its cost, followed by the total bill.

menu = input('Enter the menu items: ').split()
price = [int(x) for x in input('Enter their prices: ').split()]
order = input('Enter the order: ').split()
ordered = []
total = 0
for i in range(len(order)):
    if order[i] in ordered:
        continue
    else:
        for j in range(len(menu)):
            if order[i] == menu[j]:
                print(menu[j], 'x', order.count(order[i]), '=', order.count(order[i])*price[j])
                total += order.count(order[i])*price[j]
        ordered.append(order[i])
print('Total:', total)
'''
'''
#7
#Read a sentence and print it with every word reversed, 
#keeping the words in their original order.

s = input('Enter a sentence: ').split()
for i in s:
    print(i[::-1], end = ' ')
'''
'''
#8
#Read a string and build a list of all the digits present in it, as integers, 
#in the order they appear. Print the list and the sum of the digits.

s = input('Enter a sentence: ')
l = []
total = 0
for i in s:
    if i.isdigit():
        l.append(i)
        total += int(i)
    else:
        continue
l = [int(x) for x in l]
print(l)
print('Sum:', total)
'''
'''
#9
#The IT cell is creating college email IDs for newly admitted students. An email ID is the first
#name and last name in lowercase, joined by a dot, followed by @jklu.edu.in. If the same
#name has already been given an ID, the second student with that name gets the number 2
#after the last name, the third gets 3, and so on. Names are compared without regard to case.

n = int(input('Enter a number of students: '))
names = []
for i in range(n):
    name = input('Enter a name: ')
    name = name.lower()
    first_last = name.split()
    first = first_last[0]
    last = first_last[1]
    if name in names:
        print(f"{first}.{last}{1 + names.count(name)}@jklu.edu.in")
        names.append(name)
    else:
        print(f"{first}.{last}@jklu.edu.in")
        names.append(name)
'''
'''
#10
#Read a list of integers and move all the zeroes to the end of the list,
#keeping the other numbers in their original order. Print the list.

l1 = [int(x) for x in input('Enter the numbers: ').split()]
l2 = []
for i in l1:
    if i != 0:
        l2.append(i)
zeroes = l1.count(0)
for i in range(zeroes):
    l2.append(0)
print(l2)
'''
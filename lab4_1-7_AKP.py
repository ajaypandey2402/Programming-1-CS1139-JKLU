'''
#1
#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and years of service and print the net bonus amount.

salary = int(input('Enter the amount of salary: '))
years = int(input('Enter the amount of years: '))
if years > 5:
    bonus = 0.05*salary
    print('The bonus is:', bonus)
else:
    print('No bonus')
'''   
'''
#2
#Write a program that reads input data from the console - a password (one line of random text)
#and checks if the input matches the phrase "s3cr3t!P@ssw0rd". If it matches, print "Welcome",
#otherwise print "Wrong password!".

password = input('Enter the password: ')
if password == 's3cr3t!P@ssw0rd':
    print('Welcome')
else:
    print('Wrong password')
'''
'''
#3
#Write a program that reads input data from the console - the measures of a geometric
#shape and calculates its area. There are four types of
#shapes: square, rectangle, circle and triangle.
#The first line of input is the type of shape (square, rectangle, circle, triangle):
#If the shape is a square, the next argument will be one number - the length of its side.
#If the shape is a rectangle, the next argument will be two numbers - the lengths of its sides.
#If the shape is a circle, the next argument will be one number - the radius of the circle.
#If the shape is a triangle, the next argument will be two numbers - its base and the
#corresponding altitude.
#The result should be rounded up to the third decimal point.

shape = input('Input the type of shape: ')
if shape == 'square':
    length = int(input('Input the length: '))
    area = length**2
    print(f"The area is: {area:.3f}")
elif shape == 'rectangle':
    lengths = input('Input the lengths: ').split()
    length1 = int(lengths[0])
    length2 = int(lengths[1])
    area = length1*length2
    print(f"The area is: {area:.3f}")
elif shape == 'circle':
    radius = int(input('Input the radius: '))
    area = radius**2*3.1415
    print(f"The area is: {area:.3f}")
else:
    lengths = input('Input the base and attitude: ').split()
    length1 = int(lengths[0])
    length2 = int(lengths[1])
    area = length1*length2*0.5
    print(f"The area is: {area:.3f}")
'''
'''
#4
#Write a program that reads two integers - hours and minutes based on a 24-hour day format and
#calculates what time it will be 15 minutes later. The result should be printed in the following
#format hh:mm. Hours should always be between 0 and 23, while minutes should always be
#between 0 and 59. Hours should be written with one or two digits as needed, while the minutes
#should always be written with two digits - add a leading zero, as needed. Example, Given the time
#1:46 as input, the output displayed should be 2:01.

h = int(input('Enter hours: '))
m = int(input('Enter minutes: '))
if (m < 45):
    m += 15
    print(f"{h:02d}:{m:02d}")
else:
    m = (m+15) - 60
    if h < 23:
        h += 1
        print(f"{h:02d}:{m:02d}")
    else:
        h = 0
        print(f"{h:02d}:{m:02d}")
'''
'''
#5
#A student has to travel n kilometers. He can choose between three types of transportation:
#Taxi. Starting fee: 33.58 INR. Day rate: 37.89 INR/km. Night rate: 43.17 INR/km.
#Bus. Day / Night rate: 4.32 INR/km. Can be used for distances of a minimum of 20 km.
#Train. Day / Night rate: 2.88 INR/km. Can be used for distances of a minimum of 100 km.
#Write a program that reads the number of kilometers n and period of the day (day or night) and
#calculates the price for the cheapest transport.

n = int(input('Enter the number of kilometers: '))
day = input('Enter the period of the day: ')
if day == 'day':
    taxi = 33.58 + 37.89*n
    if n >= 20:
        bus = 4.32*n
    if n >= 100:
        train = 2.88*n
else:
    taxi = 33.58 + 43.17*n
    if n >= 20:
        bus = 4.32*n
    if n >= 100:
        train = 2.88*n

if n >= 100:
    if (train < taxi) and (train < bus):
        print('The cheapest transport price is:', train)
    elif bus < taxi:
        print('The cheapest transport price is:', bus)
    else:
        print('The cheapest transport price is:', taxi) 
elif n >= 20:
    if bus < taxi:
        print('The cheapest transport price is:', bus)
    else:
        print('The cheapest transport price is:', taxi) 
else:
    print('The cheapest transport price is:', taxi)
'''
'''
#6
#Tom Cat likes to sleep all day but, unfortunately, his owner is always playing with him whenever
#he has free time. To sleep well, the norm of games that Tom has is 30,000 minutes per year. The
#time for games he has depends on the holidays that his owner has:
#• During workdays, his owner plays with him 63 minutes per day.
#• During holidays, his owner plays with him 127 minutes per day.
#Write a program that reads the number of holidays and prints whether Tom can sleep well and
#how much the difference from the norm for the current year is. It is assumed that there are 365
#days in one year.

holidays = int(input('Enter the number of holidays: '))
workdays = 365 - holidays
playtime = workdays*63 + holidays*127
if playtime > 30000:
    print('Tom does not sleep well, the difference from the norm  is', playtime - 30000, 'minutes')
else:
    print('Tom sleeps well')
'''
'''
#7
#Most of the people start planning their vacations well in advance. A young programmer from
#Bulgaria has a certain budget (BGN is the currency of Bulgaria) and spare time in a particular
#season.
#Write a program that accepts as input the budget and season and as output displays
#programmer's vacation place and the amount of money they will spend.
#The budget determines the destination, and the season determines what amount of the budget
#will be spent. If the season is summer, the programmer will go camping, if it is winter – he will stay
#in a hotel. If it is in Europe, regardless of the season, the programmer will stay in a hotel. Each
#camp or hotel, according to the destination, has its price, which corresponds to a particular
#percentage of the budget:
#• If 100 BGN or less – somewhere in Bulgaria.
#Summer – 30% of the budget
#Winter – 70% of the budget.
#• If 1000 BGN or less – somewhere in the Balkans.
#Summer – 40% of the budget.
#Winter – 80% of the budget.
#• If more than 1000 BGN – somewhere in Europe.
#Upon traveling in Europe, regardless of the season, the programmer will
#spend 90% of the budget.

budget = int(input('Enter the budget in BGN: '))
season = input('Enter the season: ')
if budget > 1000:
    print('The vacation place is Europe, the amount to be spent is', budget*0.9)
elif budget > 100:
    if season == 'summer':
        print('The vacation place is Balkans, the amount to be spent is', budget*0.4)
    else:
        print('The vacation place is Balkans, the amount to be spent is', budget*0.8)
else:
    if season == 'summer':
        print('The vacation place is Bulgaria, the amount to be spent is', budget*0.3)
    else:
        print('The vacation place is Bulgaria, the amount to be spent is', budget*0.7)
'''
    

    

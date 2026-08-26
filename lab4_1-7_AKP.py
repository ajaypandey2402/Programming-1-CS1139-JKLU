'''
#1
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
password = input('Enter the password: ')
if password == 's3cr3t!P@ssw0rd':
    print('Welcome')
else:
    print('Wrong password')
'''

#3
'''
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
#6
'''
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
    

    
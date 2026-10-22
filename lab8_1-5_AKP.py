'''
#1
#Read a string and count how many characters in it are vowels, 
#consonants, digits, spaces and other symbols.

s = input('Enter a string: ')
vowels = 'aeuio'
count_vow = 0
count_cons = 0
digits = '1234567890'
count_dig = 0
space = ' '
count_spac = 0
others = 0
s = s.lower()
for i in s:
    if ord(i) >= 97 and ord(i) <= 122:
        if i in vowels:
            count_vow += 1
        else:
            count_cons += 1
    elif i in digits:
        count_dig += 1
    elif i == space:
        count_spac += 1
    else:
        others += 1
print('Vowels:', count_vow)
print('Consonants:', count_cons)
print('Digits:', count_dig)
print('Spaces:', count_spac)
print('Others:', others)
'''
'''
#2
#Read a string and rewrite it so that the characters at even positions 
#(0, 2, 4, …) are in uppercase and those at odd positions are in lowercase. 
#Characters that are not letters stay unchanged but still occupy a position.

s = input('Enter a string: ')
s = s.lower()
new_string = ''
for i in range(len(s)):
    if i%2 == 0:
        new_string += s[i].upper()
    else:
        new_string += s[i]
print('The new string is: ', new_string)
'''
'''
#3
#JKLU's student portal is rolling out a new sign-up page. 
#Before an account is created, the portal rates the password the student types. 
#It looks for four kinds of characters: an uppercase letter,
#a lowercase letter, a digit, and a special character (anything that is not a letter, 
#digit or space). A password shorter than 8 characters is always WEAK. 
#Otherwise it is STRONG if all four kinds are present, MODERATE if two or three kinds are present, 
#and WEAK if only one kind is present.

password = input('Enter a password: ')
count_upper = 0
count_lower = 0
count_dig = 0
count_spec = 0

for i in password:
    if i.isupper():
        count_upper += 1
    elif i.islower():
        count_lower += 1
    elif i.isdigit():
        count_dig += 1
    elif i.isspace() == 0:
        count_spec += 1
if count_upper != 0:
    count_upper = 1
if count_lower != 0:
    count_lower = 1
if count_dig != 0:
    count_dig = 1
if count_spec != 0:
    count_spec = 1
    
total_conditions = count_upper + count_lower + count_dig + count_spec
        
if (len(password) < 8) or (total_conditions == 1):
    print('WEAK')
elif total_conditions >= 2 and total_conditions <= 3:
    print('MODERATE')
elif total_conditions == 4:
    print('STRONG')
'''
'''
#4
#Read a string and a single character. 
#Print how many times the character occurs in the string and the index of every occurrence. 
#If it does not occur, print -1 for the positions.

s = input('Enter a string: ')
s = s.lower()
ch = input('Enter a character: ')
ch = ch.lower()
count_ch = 0
positions = ''
for i in range(len(s)):
    if s[i] == ch:
        count_ch += 1
        if positions == '':
            positions += str(i)
        else:
            positions += ' ' + str(i)
if count_ch == 0:
    print('Count:', 0)
    print('Positions:', -1)
else:
    print('Count:', count_ch)
    print('Positions:', positions)
'''
'''
#5
#Read a sentence and print the length of each word in it, in order, on one line. 
#Words are separated by one or more spaces, and the sentence may begin or end with spaces.

s = input('Enter a string: ')
current_word = ''
current_length = 0
total = ''
for i in range(len(s)):
    if (s[i] == ' ') and (i != len(s) - 1):
        if current_word != '':
            current_length = len(current_word)
            if total != '':
                total += ' ' + str(current_length)
            else:
                total += str(current_length)
            current_word = ''
    elif i == len(s) - 1:
        if current_word != '':
            current_length = len(current_word) + 1
            if total != '':
                total += ' ' + str(current_length)
            else:
                total += str(current_length)
            current_word = ''
    else:
        current_word += s[i]
print('Lengths of each word are:', total)
'''

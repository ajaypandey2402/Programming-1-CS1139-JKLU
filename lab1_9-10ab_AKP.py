#9 
#Input the number of seconds (1–86400) and display the equivalent time in
#HH:MM:SS format.
'''
seconds = int(input('Input the number of seconds (1-86400): '))
hours = seconds // 3600
minutes = (seconds - hours*3600)//60
seconds = seconds - hours*3600 - minutes*60
print(hours,':', minutes,':', seconds, sep="")
'''

#10 a) Attendance Percentage Calculator (eligible if attendance ≥75%)
'''
attended_classes = int(input('Input the number of classes attended: '))
overall_classes = int(input('Input the total amount of classes: '))
if (attended_classes/overall_classes)*100 >= 75:
    print('The student is eligible')
else:
    print('The student is not eligible')
'''

#10 b) Simple Electricity Bill Calculator
'''
current = int(input('Inpunt current electricity meter readings(in kWh): '))
previous = int(input('Inpunt previous electricity meter readings(in kWh): '))
total = current - previous
payment = 0
if total > 300:
    payment = (total - 300)*8 + (300 - 100)*6.5 + 100*4
else:
    if total > 100:
        payment = (total - 100)*6.5 + 100*4
    else:
        payment = total*4
print('The total paument amount is', payment+100, 'rupees')
'''

"""
Input name, hours worked per week, and hourly salary.
If hours worked > 40, multiply the following hours' salary by 1.5 
"""
print(__doc__)

employeeName = (input("Enter your name: "))
hoursWorked = float(input("Enter how many hours you work per week:"))
hourlyRate = float(input("Enter your hourly rate: "))
maxHoursBeforeOvertime = 40
 

if hoursWorked > 40:
   totalPay = (float)(((hoursWorked-40)*(hourlyRate*1.5)) + (maxHoursBeforeOvertime * hourlyRate))

else:
   totalPay = (float)(hoursWorked * hourlyRate)
   print(totalPay)

print( employeeName, "should be paid ${:,.2f} per week".format(totalPay))



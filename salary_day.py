#
# Find Salary Day for any year, based on user input
# Author: Vignesh Narasimhulu
#
# n is salary day if n falls on Monday to Friday
# (n-1) is salary day if n is Saturday
# (n-2) is salary day if n is Sunday
#

#work with days, week, month
import calendar
import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#regex match
import re

#use sys to exit
import sys

#################
##FUNCTION BEGIN
#################
# leap year function - not used in this script to take any action, but just to print on screen
def leap(x):
 p=re.compile('.000')
 m=p.match(str(x))
 if m:
  #print("1000 year pattern matched")
  y=int(x)%400
 else:
  #print ("1000 year pattern not matched")
  y=int(x)%4

 if (y == 0):
  #print ("leap")
  return 0
 else:
  #print ("noleap")
  return 1

#################
##FUNCTION END
#################

###########################
## MAIN Script beings here
###########################
today = date.today()
#determine which year we are in
year = today.year
lcheck=leap(year)
if (lcheck == 0):
 print ("We are in a leap year: " +str(year) + "\n")
else:
 print ("We are not in a Leap year: " +str(year) + "\n")

#print("The current year is: " + str(year) + "\n")
print ("Assumptions:\n1. If your pay day falls on weekday, salary will be credited on the same day\n2. If the pay day falls on weekend, salary will be credited on Friday.\n")

#define the pay day
try:
    payday=int(input("What is your usual pay day? [1-31]: "))
except ValueError:
    print("Please re-run the script and provide a valid integer as input. Thanks!")
    sys.exit("Quitting")

if re.match("^(3[01]|[12][0-9]|[1-9])$",str(payday)):    
    print("Your usual pay day is: " + str(payday) + "\n")
else:
    print("Please provide a valid day of the month [1-31]\n")
    sys.exit()

#calendar.weekday(year, month, day)
print("In the year " + str(year) + ", Salary will be credited on: ")
for m in range(1,13):
 month=calendar.month_name[m]
 lastday=calendar.monthrange(year,m)[1]
 #print ("Last day is: " + str(month) + str(lastday))
 diff=payday-lastday
 if (diff > 0):
     #print("As this month " +str(month) +" has less days than usual pay day, Pay for this month will be received on the last working day of the month\n")
     cday=calendar.weekday(year, m, lastday)
     if (cday == 6):
         pday=int(lastday-2)
         print("%10s %2d" % (month, pday))
         continue
     elif (cday == 5):
         pday=int(lastday-1)
         print("%10s %2d" % (month, pday))
         continue
     else:
         pday=lastday
         print("%10s %2d" % (month, pday))
         continue
 #else:
     #print(str(month) + ": proceed with next")

 #Determine first 3 letters of the month to compare it later with salary day's month
 smo=month[0:3]
 #output of below command is a number, where 0 is Monday
 day=calendar.weekday(year, m, payday)
 #print(day)
 # days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
 if (day == 6):
  #using timedelta approach is foolproof if salary day is 2 or 1
  xday=datetime(year, m, payday)
  yday=timedelta(days=2)
  #yyyy-mm-dd hh:mm:ss  2018-03-10 00:00:00
  tpday=xday-yday
  #strftime converts datetime to string in a readable format
  xpday=tpday.strftime('%d%b')
  ypday=xpday[2:5]
  if ( smo == ypday):
      pday=xpday[0:2]
  else:
      pday=xpday
  print(" " +str(month)+ "  " +str(pday))
 elif (day == 5):
  xday=datetime(year, m, payday)
  yday=timedelta(days=1)
  tpday=xday-yday
  xpday=tpday.strftime('%d%b')
  ypday=xpday[2:5]
  if ( smo == ypday):
      pday=xpday[0:2]
  else:
      pday=xpday
  print(" " +str(month)+ "  " +str(pday))
 else:
  pday=payday
  print("%10s %2d" % (month, pday))

#Write a Python program to calculate the number of days between two dates.
#Sample dates : (20200702), (20200711)

from datetime import date
n = (input())
m = (input())
f_date = date(int(n[:4]), int(n[4:6]), int(n[6:]))
l_date = date(int(m[:4]), int(m[4:6]), int(m[6:]))
delta = l_date - f_date
print(delta.days)
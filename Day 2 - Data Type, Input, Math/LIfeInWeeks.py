# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

rem = 90 - int(age)

days_left = int(rem * 365)
months_left = int(rem * 12)
weeks_left = int(rem * 52)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
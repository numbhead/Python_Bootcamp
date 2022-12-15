# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

t = name1_lower.count('t') + name2_lower.count('t')
r = name1_lower.count('r') + name2_lower.count('r')
u = name1_lower.count('u') + name2_lower.count('u')
e = name1_lower.count('e') + name2_lower.count('e')

l = name1_lower.count('l') + name2_lower.count('l')
o = name1_lower.count('o') + name2_lower.count('o')
v = name1_lower.count('v') + name2_lower.count('v')

first_digit = t + r + u + e
second_digit = l + o + v + e

per = str(first_digit)+str(second_digit)
per_val = int(per)

if(per_val < 10 or per_val > 90):
    print(f"Your score is {per_val}, you go together like coke and mentos.")
elif (per_val >=40 and per_val <= 50):
    print(f"Your score is {per_val}, you are alright together.")
else:
    print(f"Your score is {per_val}.")


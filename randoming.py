# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num_items = len(names)
# 🚨 Don't change the code above 👆
random_name= random.randint(0, num_items-1) 
person_who_will_pay = names[random_name]
print(f"{person_who_will_pay} pay the bill")

#Write your code below this line 👇

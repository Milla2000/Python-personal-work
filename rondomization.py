#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random	 

test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)

# if test_seed <0 and test_seed >1:
#     print("invalid input")
# else:
# you can also use random.choice()
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")


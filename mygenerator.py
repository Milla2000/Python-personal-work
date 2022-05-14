import random
import string
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
random.shuffle(characters)#shuffling characters

length = int(input("Enter password length: "))

password = []## picking random characters from the list of characters
for i in range(length):
	password.append(random.choice(characters))

random.shuffle(password)#shuffling password
print("".join(password))
#difficult level nanii huwezi elewa😂👀😂- go and read bruh
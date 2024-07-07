import random,string

pass_len = int(input("enter your password length: "))
# list = [string.ascii_letters,string.digits,string.punctuation]
charValues = string.ascii_letters + string.digits + string.punctuation
password = ""
# for i in range(pass_len):
#     # print(random.choice(charValues))
#     password +=random.choice(charValues)
# print("Your random password is: ",password)

# using list comprehension
result = "".join(random.choice(charValues) for i in range(pass_len))
print("your random password is:",result)
import random
import string
print("SAMPLE PASSWORD GENERATOR")
letters=string.ascii_letters
num=string.digits
special_char='!@#$%^&*_'
combine=letters +num+special_char
len=int(input("Enter the length of password required :"))
x=random.sample(combine,len)
password="".join(x)
print(password)

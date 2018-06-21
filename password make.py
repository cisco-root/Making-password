#######################################################
####################by Mr.jailbreak####################
#######################################################
import string 
from random import *
	 
char = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(char) for x in range(randint(8,16)))
print("this your password : " , password)
print(" <------------------>")
print(" |  by cisco root   |")
print(" <------------------>")

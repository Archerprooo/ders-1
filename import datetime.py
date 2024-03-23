import datetime
import random
a = datetime.datetime.now().strftime("%d")
b = datetime.datetime.now().strftime("%m")
c = datetime.datetime.now().strftime("%y")
a = random.randint(1,31)
b = random.randint(1,12)
c = random.randint(2024,2029)
print ("randevunuz = ",a,b,c)
    

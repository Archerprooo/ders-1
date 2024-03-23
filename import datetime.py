import datetime
import random
import time
a = datetime.datetime.now().strftime("%d")
b = datetime.datetime.now().strftime("%m")
c = datetime.datetime.now().strftime("%y")
d = int(input("doğduğun yılın son iki hanesi ne " ))
e = int(input("doğduğun ay ne "))
f = int(input("doğduğun gün ne "))
g = int(a) - f
l = int(b) - e
y = int(c) - d
print ("hayatta olduğun zaman",g,l,y)
    

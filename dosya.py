abc = open("rehber.txt","w")
for a in range (100):
    abc.write(f"{a}")
abc.close()
try:
    abc =open("rehber.txt","r")
    print(abc.read())
    abc.close()
except:
    print("hata")                               
an = 1

print ("1. basamak")
def birinci():
    an = 2
    ikinci()
    print (an)
    print ("1. basamak")
    def ikinci():
        print ("2. basamak")
        an = 3
        print (an)

birinci()
print (an)



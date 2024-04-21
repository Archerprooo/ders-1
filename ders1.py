an = 1

print ("1. basamak")
def a():
    an = 2
    b ()
    print (an)
    print ("1. basamak")
    def b():
        print ("2. basamak")
        an = 3

a ()
print (an)



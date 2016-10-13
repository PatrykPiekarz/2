a=6
b=5
if a<4:
    print a
elif a>4:
    print b
for x in range (-10,11):
    print "%+i" %x,

print "\n"

for x in range(5, 100, 10):
    print "%3i%6o%5x" % (x, x, x) #wyrownanie prawe

for x in range(5, 100, 10):
    print "%-3i%#-6o%#-5x" % (x,x,x) #wyrownanie lewe (#-wlasiwy prefiks)

for x in range(5,100,10):
    print "%3i %#04o %#04x" % (x,x,x) #0 - pole na liczby bedzie wypelnione zerami

a=[1,2,3,4,5,6]
while a:
    a=a[:len(a)-1]
    print a

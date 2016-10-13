#wyswietl tabliczke mnozenia

for x in range (1,11):
    print "%3i" % (x),
    for y in range (2,11):
        if x == 1: print "%3i" % (x*y),
        print "%3i" % (x*y),
    print "\n"
#fibonacci
lst = [0,1]
n = int(raw_input("podaj dlugosc ciagu"))
print lst[0],"\n",lst[1]
for i in range (2,n):
    lst.append(lst[i-1]+lst[i-2])
    print lst[i]
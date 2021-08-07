#def genf():
    #for i in [43,65,32]:
        #yield i

#s = genf()
#print(s)
#print(next(s))
#print(next(s))
#print(next(s))
#print(next(s))


#def genf():
    #for i in [43,65,32]:
        #yield i

#for i in genf():
    #print(i)


#def genf():
    #s=7
    #for i in [43,65,32]:
        #yield i
        #print(s)
        #s=s*10+7


#g = genf()
#print(next(g))
#print(next(g))
#print(next(g))


def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr=pr*i
        yield pr


for i in fact(10):
    print(i, end=' ')


#s =fact(10)
#print(next(s))
#print(next(s))
#print(next(s))
#print(next(s))
#print(next(s))
#print(next(s))
#print(next(s))
#print(next(s))
#print(next(s))
#print(next(s))
#print(next(s))











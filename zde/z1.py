from itertools import groupby


def group_consecutives(vals, step=1):
    """Return list of consecutive lists of numbers from vals (number list)."""
    run = []
    result = [run]
    expect = None
    for v in vals:
        if (v == expect) or (expect is None):
            run.append(v)
        else:
            run = [v]
            result.append(run)
        expect = v + step
    return result


L = [0, 0, 0, 3, 3, 2, 5,5, 2, 6, 6, 7,7]
grouped_L = [(k, sum(1 for i in g)) for k,g in groupby(L)]
 # Or (k, len(list(g))), but that creates an intermediate list
#print grouped_L
sl= set(L)
lsl=len(sl)
ded = []
for x in sl:
    #print x, L.count(x)
    if(L.count(x)>1):
        ded.append(x)

#print ded

#print type(group_consecutives(ded))

run = []
result = [run]
expect = None
for v in ded:
    if (v == expect) or (expect is None):
        run.append(v)
    else:
        run = [v]
        result.append(run)
    expect = v + 1
    #return result
print result

count = 0
for r in result:
    #print type(r)
    if (len(r)>=3):
        count = count+1
        
if (count>0):
    print "yes"
        
        
        

#
#for i in range(0, len(ded)):
#    a = ded[i]
#    fl = 0
    #print a
    #j = i+1
    #b = ded[j]
    #if(b==a+1 and L.count(a)>0 and L.count(b)>0):
    #    fl = fl+1
    

    
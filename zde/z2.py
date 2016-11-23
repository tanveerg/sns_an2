arr = [[2,1],
        [3,1], [4,2], [5,3]]

x = []
y = []
out = []

for d in arr:
    temp = []
    #print d
    x.append(d[0])
    if (len(d)>1):
        y.append(d[1])
    #if (d[0] not in out and d[1] not in out):
    #    #temp.append(d[1])
    #    temp.append(d[0])
    #    temp.append(d[1])
    #    out.append(temp[1])
    #    out.append(temp[0])
for y1 in y:
    if (y1 not in out):
        out.append(y1)
print out[len(out)-1]    
for x1 in x:
    if (x1 not in out):
        out.append(x1)    
    
    #x.append(d[0])
    #y.append(d[1])
print out
out.reverse()
print out
#print list(set(out))
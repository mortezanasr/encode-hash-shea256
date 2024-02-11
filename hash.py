import hashlib
import csv

ss = dict()
for i in range(0 ,9999):
    ii = str(i)
    a_Hash = hashlib.sha256(str(ii).encode('utf-8'))
    ss[i] = a_Hash.hexdigest()
 
with open('/home/morteza/Documents/h.csv') as f:
    a = csv.reader(f)
    c = list()
    d = list()
    for row in a:
        c.append(row[1])
        d.append(row[0])
        
        q = c.pop()
        w = d.pop()
        
        for a in ss:
            b = str(ss[a])
            if b == q:
                
                print("ramzeh %s adade %i mibashad" %(w,int(a)))
                break
    
         

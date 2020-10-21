d = dict() 
li=list()

#li=['eat','ate','apt','pat','tea','now'] #given list of examples

x=None
while x!='done': #taking input from user till he enters 'done'
    x=input()
    if x!='done':
        li.append(x)
    
for i in li:
    temp = " ".join(sorted(list(i))) #sorting individual element of list and joining back in string
    if temp not in d: 
        d[temp] =[i]   
    else:
        d[temp] +=[i]
ana=list()
for j in d.values(): #to obtain only values 
    ana.append(j)
print(ana)


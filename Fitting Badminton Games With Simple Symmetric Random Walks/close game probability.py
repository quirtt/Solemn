import math
A=[]
prob=[]
for m in range(19):
    x=math.comb(2*m,m)*(math.comb(39-2*m,19-m)-math.comb(39-2*m,18-m))/(m+1)
    A.append(x)
x=math.comb(38,19)*math.comb(1,0)/(20)
A.append(x)
for k in range(1,21):
    y=0
    for j in range(20-k,20):
        y+=A[j]
    y=y/(math.comb(40,21))
    prob.append(y)
print(prob)
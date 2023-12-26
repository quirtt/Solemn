p=numeric(21)
for (k in 0:20){
  p[k+1]=choose((20+k),k)/2^(20+k)
}
mat=matrix(numeric(21*11),21,11)
for (x in 0:10){
  for (y in 0:20){
    if (x<=y & y<11){
      a=21+y-11-x
      mat[(y+1),(x+1)]=choose(a-1,9)/(2^(a))}
    else if (x<y & 11<=y){
      a=10+y-x
      mat[(y+1),(x+1)]=(choose(a-1,9)+choose(a-1,20-x))/(2^a)}}}
q=mat
for (i in 0:20){
  q[i,]=q[i,]/p[i]
}
maxi=numeric(11)
change=numeric(11)
for (i in 1:11){
  maxi[i]=max(q[,i])
  for (j in 1:21){
    if (q[j,i]==maxi[i]){
      change[i]=j}}
}
e=0.1
indicator=matrix(numeric(21*11),21,11)
for (i in 1:21){
  for (j in 1:11){
    if (q[i,j]+e<maxi[j] ){
      indicator[i,j]=1
    }}
}
expense=0
win=0
for (n in 1:1000){
  expense=expense+1
i=sample(0:20,1,prob=p)
  a=0
  b=0
  for (j in 1:21){
    x=sample(2,1)
    if (x==1){
      a=a+1
      if (a==11){break}}
      else{
        b=b+1
        if (b==11){break}}}
  y=min(a,b)
  if (indicator[i+1,y+1]==1){
    expense=expense+e
    i=change[y+1]}
  for (j in 1:30){
    x=sample(2,1)
    if (x==1){
      a=a+1
      if (a==21){break}}
      else{
        b=b+1
        if (b==21){break}}
  }
  y=min(a,b)
  if (y==i){
    win=win+(1/p[i+1])
  }
}
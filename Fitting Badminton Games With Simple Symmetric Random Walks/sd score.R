s=numeric(21)
for (m in 0:20){
dev=numeric(1000)
for (n in 1:1000){
  score=0
for (t in 1:1000){
a=0
b=0
for (j in 1:41){
  x=sample(2,1)
  if (x==1){
    a=a+1
    if (a==21){break}}
  else{
    b=b+1
    if (b==21){break}}
}
y=min(a,b)
if (m==y){
score=score+1}}
  dev[n]=score}
s[m+1]=sd(dev/1000)}

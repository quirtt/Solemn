s=numeric(20)
for (t in 1:20){
dev=numeric(500)
for (n in 1:500){
time=numeric(1283)
for (k in 1:1283){
run=rep(1,40)
toss=sample(40,21)
for (i in toss){
  run[i]=-1
}
lead=numeric(40)
for (j in 1:40){
  lead[j]=sum(run[1:j])
}
count=0
for (i in 1:40){
  if (i>1){
    if (lead[i]>=0 & lead[i-1]>=0){
      count=count+1
    }
  }
  else{
    if (lead[i]>=0){count=count+1}
  }
}
time[k]=count}
dev[n]=sum(time==2*t)/1283}
s[t]=sd(dev)}
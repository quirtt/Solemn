data=read.csv("Bad.csv")
count=0
for (i in 1:5027){
  if (data[,(3*i)][40]==2){
    count=count+1}}
print(count)


data=read.csv("Bad.csv")
count=c()
for (i in 1:5027){
  count1=40
  if (data[,3*i][40]==0){
    for (j in 1:40){
      if(j>1){
        if (data[,(i*3)][j-1]<=0 & data[,(i*3)][j]<=0){
          count1=count1-1
        }}
      else{
        if (data[,(3*i)][j]<=0){
          count1=count1-1}}}
    count=c(count,count1)}
}
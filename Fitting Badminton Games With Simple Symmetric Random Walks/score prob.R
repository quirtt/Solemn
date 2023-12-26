p=numeric(21)
for (k in 0:20){
  p[k+1]=choose((20+k),k)/2^(20+k)
}
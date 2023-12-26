import pandas as pd
col=['game_1_scores','game_2_scores','game_3_scores']
data=pd.read_csv('md.csv',usecols=col)
game1=data['game_1_scores']
game2=data['game_2_scores']
game3=data['game_3_scores']
chose=[]
for i in range(len(game1)):
    ls=str(game1[i])
    A=ls.split(',')
    a=A[-1]
    a=a.replace(']','')
    b=A[0]
    b=b.replace('[','')
    A[0]=b
    A[-1]=a
    for j in range(len(A)):
        a=A[j]
        a=a.replace("'","")
        A[j]=a 
    game1[i]=A
for j in range(len(game1)):
    if len(game1[j])==43:
        chose.append(game1[j])
for i in range(len(game2)):
    ls=str(game2[i])
    A=ls.split(',')
    a=A[-1]
    a=a.replace(']','')
    b=A[0]
    b=b.replace('[','')
    A[0]=b
    A[-1]=a
    for j in range(len(A)):
        a=A[j]
        a=a.replace("'","")
        A[j]=a 
    game2[i]=A
for j in range(len(game2)):
    if len(game2[j])==43:
        chose.append(game2[j])
for i in range(len(game3)):
    ls=str(game3[i])
    A=ls.split(',')
    a=A[-1]
    a=a.replace(']','')
    b=A[0]
    b=b.replace('[','')
    A[0]=b
    A[-1]=a
    for j in range(len(A)):
        a=A[j]
        a=a.replace("'","")
        A[j]=a 
    game3[i]=A
for j in range(len(game3)):
    if len(game3[j])==43:
        chose.append(game3[j])

print(len(chose))
new=pd.DataFrame()
for k in range(len(chose)):
    x=chose[k]
    a=[[],[],[]]
    for j in range(len(x)):
        A=x[j].split('-')
        a[0].append(int(A[0]))
        a[1].append(int(A[1]))
        a[2].append(int(A[0])-int(A[1]))
    new.insert(3*k,'player A'+str(735+k),a[0][:])
    new.insert(3*k+1,'player B'+str(735+k),a[1][:])
    new.insert(3*k+2,'lead'+str(735+k),a[2][:])
new.to_csv('bad.csv',index=False)
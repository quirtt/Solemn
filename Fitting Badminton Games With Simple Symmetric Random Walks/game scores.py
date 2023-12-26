import pandas as pd
col=['game_1_scores','game_2_scores','game_3_scores']
data=pd.read_csv('wd.csv',usecols=col)
game1=data['game_1_scores']
game2=data['game_2_scores']
game3=data['game_3_scores']
chose=[]
score=[0]*21
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
    for k in range(20):
        if len(game1[j])==(21+k):
            score[k]+=1
            break
    if len(game1[j])>40:
        score[20]+=1
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
    for k in range(20):
        if len(game2[j])==(21+k):
            score[k]+=1
            break
    if len(game2[j])>40:
        score[20]+=1
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
    for k in range(20):
        if len(game3[j])==(21+k):
            score[k]+=1
            break
    if len(game3[j])>40:
        score[20]+=1
print(score)
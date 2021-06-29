import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# df1 = pd.read_csv('train.csv')
# df2 = pd.read_csv('test.csv')
# sam = pd.read_csv('sample_submission.csv')
sub1 = pd.read_csv('1.csv')
# print(vote)
# np.savetxt("vote.csv",vote,fmt='%d',delimiter=',')
# print("ok")
sub2 = pd.read_csv('2.csv')
sub3 = pd.read_csv('3.csv')
sub4 = pd.read_csv('4.csv')
sub5 = pd.read_csv('5.csv')
sub6 = pd.read_csv('6.csv')
sub7 = pd.read_csv('7.csv')
sub8 = pd.read_csv('8.csv')
sub9 = pd.read_csv('9.csv')
vote = np.zeros((9,100000))
vote1 = np.zeros((9,100000))
vote2 = np.zeros((9,100000))
vote3 = np.zeros((9,100000))
vote4 = np.zeros((9,100000))
vote5 = np.zeros((9,100000))
vote6 = np.zeros((9,100000))
vote7 = np.zeros((9,100000))
vote8 = np.zeros((9,100000))
vote9 = np.zeros((9,100000))


for i in range(100000):
    b = sub1.loc[[i]]
    b =b.drop(columns=['id'])
    c = list(b.stack().idxmax())[1]
    if(c=='Class_1'):
        vote1[0][i]+=1
        vote[0][i]+=1
    if(c=='Class_2'):
        vote1[1][i]+=1
        vote[1][i]+=1
    if(c=='Class_3'):
        vote1[2][i]+=1
        vote[2][i]+=1
    if(c=='Class_4'):
        vote1[3][i]+=1
        vote[3][i]+=1
    if(c=='Class_5'):
        vote1[4][i]+=1
        vote[4][i]+=1
    if(c=='Class_6'):
        vote1[5][i]+=1
        vote[5][i]+=1
    if(c=='Class_7'):
        vote1[6][i]+=1
        vote[6][i]+=1
    if(c=='Class_8'):
        vote1[7][i]+=1
        vote[7][i]+=1
    if(c=='Class_9'):
        vote1[8][i]+=1
        vote[8][i]+=1
    if i%1000==0:
        print("i:",i)
np.savetxt("vote1.csv",vote1.T,fmt='%d',delimiter=',')
print("1 ok")

for i in range(100000):
    b = sub2.loc[[i]]
    b =b.drop(columns=['id'])
    c = list(b.stack().idxmax())[1]
    if(c=='Class_1'):
        vote2[0][i]+=1
        vote[0][i]+=1
    if(c=='Class_2'):
        vote2[1][i]+=1
        vote[1][i]+=1
    if(c=='Class_3'):
        vote2[2][i]+=1
        vote[2][i]+=1
    if(c=='Class_4'):
        vote2[3][i]+=1
        vote[3][i]+=1
    if(c=='Class_5'):
        vote2[4][i]+=1
        vote[4][i]+=1
    if(c=='Class_6'):
        vote2[5][i]+=1
        vote[5][i]+=1
    if(c=='Class_7'):
        vote2[6][i]+=1
        vote[6][i]+=1
    if(c=='Class_8'):
        vote2[7][i]+=1
        vote[7][i]+=1
    if(c=='Class_9'):
        vote2[8][i]+=1
        vote[8][i]+=1
    if i%1000==0:
        print("i:",i)
np.savetxt("vote2.csv",vote2.T,fmt='%d',delimiter=',')
print("2 ok")

for i in range(100000):
    b = sub3.loc[[i]]
    b =b.drop(columns=['id'])
    c = list(b.stack().idxmax())[1]
    if(c=='Class_1'):
        vote3[0][i]+=1
        vote[0][i]+=1
    if(c=='Class_2'):
        vote3[1][i]+=1
        vote[1][i]+=1
    if(c=='Class_3'):
        vote3[2][i]+=1
        vote[2][i]+=1
    if(c=='Class_4'):
        vote3[3][i]+=1
        vote[3][i]+=1
    if(c=='Class_5'):
        vote3[4][i]+=1
        vote[4][i]+=1
    if(c=='Class_6'):
        vote3[5][i]+=1
        vote[5][i]+=1
    if(c=='Class_7'):
        vote3[6][i]+=1
        vote[6][i]+=1
    if(c=='Class_8'):
        vote3[7][i]+=1
        vote[7][i]+=1
    if(c=='Class_9'):
        vote3[8][i]+=1
        vote[8][i]+=1
    if i%1000==0:
        print("i:",i)
np.savetxt("vote3.csv",vote3.T,fmt='%d',delimiter=',')
print("3 ok")

for i in range(100000):
    b = sub4.loc[[i]]
    b =b.drop(columns=['id'])
    c = list(b.stack().idxmax())[1]
    if(c=='Class_1'):
        vote4[0][i]+=1
        vote[0][i]+=1
    if(c=='Class_2'):
        vote4[1][i]+=1
        vote[1][i]+=1
    if(c=='Class_3'):
        vote4[2][i]+=1
        vote[2][i]+=1
    if(c=='Class_4'):
        vote4[3][i]+=1
        vote[3][i]+=1
    if(c=='Class_5'):
        vote4[4][i]+=1
        vote[4][i]+=1
    if(c=='Class_6'):
        vote4[5][i]+=1
        vote[5][i]+=1
    if(c=='Class_7'):
        vote4[6][i]+=1
        vote[6][i]+=1
    if(c=='Class_8'):
        vote4[7][i]+=1
        vote[7][i]+=1
    if(c=='Class_9'):
        vote4[8][i]+=1
        vote[8][i]+=1
    if i%1000==0:
        print("i:",i)
np.savetxt("vote4.csv",vote4.T,fmt='%d',delimiter=',')
print("4 ok")

for i in range(100000):
    b = sub5.loc[[i]]
    b =b.drop(columns=['id'])
    c = list(b.stack().idxmax())[1]
    if(c=='Class_1'):
        vote5[0][i]+=1
        vote[0][i]+=1
    if(c=='Class_2'):
        vote5[1][i]+=1
        vote[1][i]+=1
    if(c=='Class_3'):
        vote5[2][i]+=1
        vote[2][i]+=1
    if(c=='Class_4'):
        vote5[3][i]+=1
        vote[3][i]+=1
    if(c=='Class_5'):
        vote5[4][i]+=1
        vote[4][i]+=1
    if(c=='Class_6'):
        vote5[5][i]+=1
        vote[5][i]+=1
    if(c=='Class_7'):
        vote5[6][i]+=1
        vote[6][i]+=1
    if(c=='Class_8'):
        vote5[7][i]+=1
        vote[7][i]+=1
    if(c=='Class_9'):
        vote5[8][i]+=1
        vote[8][i]+=1
    if i%1000==0:
        print("i:",i)
np.savetxt("vote5.csv",vote5.T,fmt='%d',delimiter=',')
print("5 ok")

for i in range(100000):
    b = sub6.loc[[i]]
    b =b.drop(columns=['id'])
    c = list(b.stack().idxmax())[1]
    if(c=='Class_1'):
        vote6[0][i]+=1
        vote[0][i]+=1
    if(c=='Class_2'):
        vote6[1][i]+=1
        vote[1][i]+=1
    if(c=='Class_3'):
        vote6[2][i]+=1
        vote[2][i]+=1
    if(c=='Class_4'):
        vote6[3][i]+=1
        vote[3][i]+=1
    if(c=='Class_5'):
        vote6[4][i]+=1
        vote[4][i]+=1
    if(c=='Class_6'):
        vote6[5][i]+=1
        vote[5][i]+=1
    if(c=='Class_7'):
        vote6[6][i]+=1
        vote[6][i]+=1
    if(c=='Class_8'):
        vote6[7][i]+=1
        vote[7][i]+=1
    if(c=='Class_9'):
        vote6[8][i]+=1
        vote[8][i]+=1
    if i%1000==0:
        print("i:",i)
np.savetxt("vote6.csv",vote6.T,fmt='%d',delimiter=',')
print("6 ok")

for i in range(100000):
    b = sub7.loc[[i]]
    b =b.drop(columns=['id'])
    c = list(b.stack().idxmax())[1]
    if(c=='Class_1'):
        vote7[0][i]+=1
        vote[0][i]+=1
    if(c=='Class_2'):
        vote7[1][i]+=1
        vote[1][i]+=1
    if(c=='Class_3'):
        vote7[2][i]+=1
        vote[2][i]+=1
    if(c=='Class_4'):
        vote7[3][i]+=1
        vote[3][i]+=1
    if(c=='Class_5'):
        vote7[4][i]+=1
        vote[4][i]+=1
    if(c=='Class_6'):
        vote7[5][i]+=1
        vote[5][i]+=1
    if(c=='Class_7'):
        vote7[6][i]+=1
        vote[6][i]+=1
    if(c=='Class_8'):
        vote7[7][i]+=1
        vote[7][i]+=1
    if(c=='Class_9'):
        vote7[8][i]+=1
        vote[8][i]+=1
    if i%1000==0:
        print("i:",i)
np.savetxt("vote7.csv",vote7.T,fmt='%d',delimiter=',')
print("7 ok")

for i in range(100000):
    b = sub8.loc[[i]]
    b =b.drop(columns=['id'])
    c = list(b.stack().idxmax())[1]
    if(c=='Class_1'):
        vote8[0][i]+=1
        vote[0][i]+=1
    if(c=='Class_2'):
        vote8[1][i]+=1
        vote[1][i]+=1
    if(c=='Class_3'):
        vote8[2][i]+=1
        vote[2][i]+=1
    if(c=='Class_4'):
        vote8[3][i]+=1
        vote[3][i]+=1
    if(c=='Class_5'):
        vote8[4][i]+=1
        vote[4][i]+=1
    if(c=='Class_6'):
        vote8[5][i]+=1
        vote[5][i]+=1
    if(c=='Class_7'):
        vote8[6][i]+=1
        vote[6][i]+=1
    if(c=='Class_8'):
        vote8[7][i]+=1
        vote[7][i]+=1
    if(c=='Class_9'):
        vote8[8][i]+=1
        vote[8][i]+=1
    if i%1000==0:
        print("i:",i)
np.savetxt("vote8.csv",vote8.T,fmt='%d',delimiter=',')
print("8 ok")

for i in range(100000):
    b = sub9.loc[[i]]
    b =b.drop(columns=['id'])
    c = list(b.stack().idxmax())[1]
    if(c=='Class_1'):
        vote9[0][i]+=1
        vote[0][i]+=1
    if(c=='Class_2'):
        vote9[1][i]+=1
        vote[1][i]+=1
    if(c=='Class_3'):
        vote9[2][i]+=1
        vote[2][i]+=1
    if(c=='Class_4'):
        vote9[3][i]+=1
        vote[3][i]+=1
    if(c=='Class_5'):
        vote9[4][i]+=1
        vote[4][i]+=1
    if(c=='Class_6'):
        vote9[5][i]+=1
        vote[5][i]+=1
    if(c=='Class_7'):
        vote9[6][i]+=1
        vote[6][i]+=1
    if(c=='Class_8'):
        vote9[7][i]+=1
        vote[7][i]+=1
    if(c=='Class_9'):
        vote9[8][i]+=1
        vote[8][i]+=1
    if i%1000==0:
        print("i:",i)
np.savetxt("vote9.csv",vote9.T,fmt='%d',delimiter=',')
print("9 ok")

np.savetxt("vote.csv",vote.T,fmt='%d',delimiter=',')
print("vote ok")

vote1 =  pd.read_csv('vote1.csv',header=None,names=range(1,10))
vote2 =  pd.read_csv('vote2.csv',header=None,names=range(1,10))
vote3 =  pd.read_csv('vote3.csv',header=None,names=range(1,10))
vote4 =  pd.read_csv('vote4.csv',header=None,names=range(1,10))
vote5 =  pd.read_csv('vote5.csv',header=None,names=range(1,10))
vote6 =  pd.read_csv('vote6.csv',header=None,names=range(1,10))
vote7 =  pd.read_csv('vote7.csv',header=None,names=range(1,10))
vote8 =  pd.read_csv('vote8.csv',header=None,names=range(1,10))
vote9 =  pd.read_csv('vote9.csv',header=None,names=range(1,10))
vote = pd.read_csv('vote.csv',header=None,names=range(1,10))
# print(sub1.columns[1:])
# print(sub1)
print(vote)
def gen(main):
    g = main.copy()    
    for i in range(100000):
        b = vote.loc[[i]]
        # print(b)
        max_b = b.max(axis=1)
        c = b.idxmax(axis = 1)
        # print("max:",max_b)
        # print("colum:",c)
        if i%1000==0:
            print("i:",i)
        if int(vote1.loc[i][c])==1:
            g.iloc[i]=sub1.iloc[i]
            continue
        if int(vote2.loc[i][c])==1:
            g.iloc[i]=sub2.iloc[i]
            continue
        if int(vote3.loc[i][c])==1:
            g.iloc[i]=sub3.iloc[i]
            continue
        if int(vote4.loc[i][c])==1:
            g.iloc[i]=sub4.iloc[i]
            continue
        if int(vote5.loc[i][c])==1:
            g.iloc[i]=sub5.iloc[i]
            continue
        if int(vote6.loc[i][c])==1:
            g.iloc[i]=sub6.iloc[i]
            continue
        if int(vote7.loc[i][c])==1:
            g.iloc[i]=sub7.iloc[i]
            continue
        if int(vote8.loc[i][c])==1:
            g.iloc[i]=sub8.iloc[i]
            continue
        if int(vote9.loc[i][c])==1:
            g.iloc[i]=sub9.iloc[i]
            continue
    return g

result = gen(sub1)

result.to_csv("submission.csv",index=False)

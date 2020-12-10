import tsvio
import os


folder = "../tsv"

al = []
for f in os.listdir(folder):
    al = al + tsvio.read_tsv(os.path.join(folder,f))
    
    
for k,a in enumerate(al):
    if a[1]=='1': 
        print(a,k);break


dic = {}
mismatch = []
repeated = []
for i,a in enumerate(al):
    if a[1]=='0':
        a[1]="human"
    if a[1]=='1':
        a[1]="bot"
    al[i] = a
    if a[0] in dic:
        if a[1]!=dic[a[0]][1]:
            print(a[1],dic[a[0]][1],dic[a[0]],a)
            mismatch.append(i)
            mismatch.append(dic[a[0]][3])
        else:
            repeated.append(i)
    else:
        dic[a[0]] = a+[i]
        
exclude = mismatch+repeated
corrected = [a for i,a in enumerate(al) if i not in exclude]
print("Found %i mismatches"%len(mismatch))
print("Found %i repititions"%len(repeated))
for i,a in enumerate(corrected):
    if a[1]=='1': 
        print(a,i);break


tsvio.save_tsv(os.path.join(folder, "../datasets/all_users.tsv"),corrected)

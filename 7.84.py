a=[]
win,lose,noth,cnt,s=0,0,0,0,0

for i in range(21):
    a.append(list(map(int,input().split())))
    if abs(a[i][0]-a[i][1])>=3:
        cnt+=1
    if a[i][0]>a[i][1]:
        print("ВЫИГРЫШ")
        win+=1
        s+=3
    elif a[i][0]<a[i][1]:
        print("ПРОИГРЫШ")
        lose+=1
        s+=1
    elif a[i][0]==a[i][1]:
        print("НИЧЬЯ")
        noth+=1

print("ПРОИГРЫШЕЙ || ПОБЕД || НИЧЬИ || РАЗНИЦА || ОЧКИ")
print("    ",lose,"        ",win,"      ",noth,"       ",cnt,"      ",s)

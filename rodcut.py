def buCutRod(liste,n):
    r=[0]*(n+1)
    for j in range(1,n+1):
        q=-1000
        i=1
        while (i<=j):
            if(q>liste[i]+r[j-i]):
                q=q
                i=i+1
            else:
                q=(liste[i]+r[j-i])
                i=i+1
        r[j]=q
    print (r)
    return r[n]

liste=[0,4,9,15,18,21,28,31,37];
print(buCutRod(liste,8));



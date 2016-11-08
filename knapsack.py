#Dynamic programming code solving knapsack 0-1 problem

n=100;
p=[0,3,5,7,9];
ppp=[3,5,7,9]
pp=[0,60,100,120];
r=[-1000]*(n+1);
g=set();


def knapsack(p,pp,n,r,g):
    
    g.add(n)
    if r[n]>=0:
        return r[n]
    if n==0:
        q=0
    else:
        q=-1000
        for i in range(1,len(p)):
            
            if(p[i]>n):
                break
            a=(pp[i]+knapsack(p,pp,n-p[i],r,g))
            if(q>=a):
               q=q
            else:
                q=a
    r[n]=q
    return q




def nextnumber(liste,n):
    ordbok={x:[0,x] for x in range (len(liste))}
    problem=[]
    while(1==1):
        q=100000
        for i in range(len(liste)):
            x=ordbok[i][0]
            y=ordbok[i][1]
            a=x*liste[i]+liste[y]
            if(q<a):
                q=q
            else:
                q=a
                if(y==len(liste)-1):
                    ordbok[i][0]=x+1
                    ordbok[i][1]=0
                else:
                    ordbok[i][1]=y+1
        
        problem.append(q)
        if(q>=n):
            break
    return set(problem)

#comparing number of sub-problems solved by the two methods of dynamic programming
#conclusion: BottomUp solves subproblems <n and memoizing solves always =n. Bottomup is winner
def BottomUp_vs_memo(p,pp,n,r,g,ppp):  
    print("bottom up: ");
    print(len(nextnumber(ppp,n)));
    knapsack(p,pp,n,r,g);
    print("-------------------");
    print("memoizing: ");
    print(len(g));

  


               

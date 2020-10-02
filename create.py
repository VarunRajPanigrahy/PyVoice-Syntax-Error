def solve(n,arr):
    mp  = dict()

    for i in arr:
        if(i not in mp):
            mp[i]=1
        else:
            mp[i]+=1

    ans=0
    
    for i in arr:
        if(i == 1):
            if(mp[i]>1):
                ans+=1
            continue
        flag=False
        for j in range(2,int((i**0.5))+1):
            if(i%j==0):
                k = i//j
                if(j in mp or k in mp):
                    flag=True
                
        
        if(1 in mp or mp[i]>1):
            flag=True
        
        if(flag):
            #print(i)
            ans+=1

    return ans

n = int(input())
A = list(map(int,input().split()))
x = solve(n,A)
print(x)
                
    

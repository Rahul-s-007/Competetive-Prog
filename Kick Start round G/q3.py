import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

for temp in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0

    for i in range(n):
        if a[i]>=0:
            sum=0
            for j in range(i,n):
                sum=sum+a[j]
                if(sum>=0):
                    #print(a[j])
                    ans=ans+sum
                else:
                    break
   
    print(f"Case #{temp+1}: {ans}")
    #print(ans)
    #print("-----------------------")
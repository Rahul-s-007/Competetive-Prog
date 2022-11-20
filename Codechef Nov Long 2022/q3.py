import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

"""
1 ball = 1
2 ball = 2 
3 ball = 6
4 balls = 24
"""

lst = [1,1]
for n in range(2,1000001):
    x = n*lst[n-1]
    lst.append(x % 1000000007)

for temp in range(int(input())):
    l = int(input())
    arr = [int(x) for x in input().split()]
    ans = 0
    for i in arr:
        ans += lst[i]

    print(ans % 1000000007)


"""
for temp in range(int(input())):
    l = int(input())
    arr = [int(x) for x in input().split()]
    ans = 0
    #lst = [0,1]
    lst = [1]
    
    #for n in range(2,1000000):
    for n in range(1,1000000):
        lst.append((n*lst[n-1]) % 1000000007)
    
    #print(lst[0:6])
    for i in arr:
        ans += lst[i]

    print(ans % 1000000007)
"""
"""
for temp in range(int(input())):
    l = int(input())
    arr = [int(x) for x in input().split()]
    freq = {}
    ans = 0

    def fact(n):
        if (n == 1):
            return 1
        else:
            if n in freq:
                return freq[n]
            else:
                return n*fact(n-1)

    for i in arr:
        if i not in freq:
            freq[i] = fact(i)
            ans += freq[i]
        else:
            ans += freq[i]

    #print(freq)
    print(ans % 1000000007)
"""


"""
for temp in range(int(input())):
    l = int(input())
    arr = [int(x) for x in input().split()]
    m = max(arr)+1
    ball_count = [1 for i in range(m)]

    for i in range(1,m):
        ball_count[i] = i * ball_count[i-1]
    
    #print(ball_count)
    ans = 0
    for j in arr:
        ans += ball_count[j]
    
    print(ans % 1000000007)
"""
"""
for temp in range(int(input())):
    l = int(input())
    arr = [int(x) for x in input().split()]
    m = max(arr)
    ball_count = [0 for i in range(m+1)]
    ans = 0

    def fact(n):
        if (n == 1):
            return 1
        else:
            if(ball_count[n] != 0):
                return ball_count[n]
            else:
                return n*fact(n-1)

    for i in arr:
        ball_count[i] = fact(i)
        ans = ans + ball_count[i]
    
    print(ans % 1000000007)
"""

"""
for temp in range(int(input())):
    l = int(input())
    arr = [int(x) for x in input().split()]
    m = max(arr)
    #print(arr)
    ball_count = [0 for i in range(m+1)]
    ans = 0

    def fact(n):
        if (n == 1):
            return 1
        else:
            if(ball_count[n] != 0):
                return ball_count[n]
            else:
                return n*fact(n-1)

    def check_exists(n):
        if(ball_count[n] == 0):
            ball_count[n] = fact(n)
            return ball_count[n]
        else:
            return ball_count[n]

    for i in arr:
        ans = ans + check_exists(i)
    
    print(ans % 1000000007)
"""

"""
Scanner sc = new Scanner(System.in);
		long[] lst = new long [1000001];
		lst[0] = 1;
		lst[1] = 1;
	    for(int i = 2; i< 1000001; i++)
	    {
            lst[i] = (i*lst[i-1])%1000000007	        
	    }
	    
	    int l = sc.nextInt();
	    for(int i=0;i<l;i++)
	    {
	        
	    }
"""
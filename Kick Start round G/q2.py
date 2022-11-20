import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    t = [int(x) for x in input().split()]
    rs = t[0]
    rh = t[1]
    red_pts = 0
    yellow_pts = 0

    #print("N-")
    n = int(input())
    n_pos=[]
    n_inh=[]
    for i in range(n):
        n_pos.append([int(x) for x in input().split()])
        xn=n_pos[i][0]
        yn=n_pos[i][1]
        dist = ((xn)**2 + (yn)**2)**0.5
        if(dist<=rs+rh):
            n_inh.append(dist)
            #print("in")
    
    #print("M-")
    m = int(input())
    m_pos=[]
    m_inh=[]
    for i in range(m):
        m_pos.append([int(x) for x in input().split()])
        xm=m_pos[i][0]
        ym=m_pos[i][1]
        dist = ((xm)**2 + (ym)**2)**0.5
        if(dist<=rs+rh):
            m_inh.append(dist)
            #print("in")

    n_inh.sort()
    m_inh.sort()
    #print(n_inh)
    #print(m_inh)
    if(len(n_inh)):
        n_near = n_inh[0]
    else:
        n_near = -1
    if(len(m_inh)):
        m_near = m_inh[0]
    else:
        m_near=-1

    if(n_near!=-1):
        for i in range(len(m_inh)):
            if(m_inh[i]<n_near):
                yellow_pts=yellow_pts+1
            else:
                break
    else:
        yellow_pts=yellow_pts+len(m_inh)
    
    if(m_near!=-1):
        for i in range(len(n_inh)):
            if(n_inh[i]<m_near):
                red_pts=red_pts+1
            else:
                break
    else:
        red_pts=red_pts+len(n_inh)
    
    print(f"Case #{temp+1}: {red_pts} {yellow_pts}")
    #print(red_pts,yellow_pts)
    #print("-----------------------------")
    #print(rs,rh,n,m)
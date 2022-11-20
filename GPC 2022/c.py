import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

while True:
    d,r = [int(x) for x in input().split()]

    #print(bin(d)[2::].zfill(24))
    #print(bin(r)[2::].zfill(24))
    #print(bin(d^r)[2::].zfill(24))

    if(d==0 and r==0):
        break
    z = int("000000000000000000000000",2)
    o = int("111111111111111111111111",2)

    #print(str(bin(d^r)[2::].zfill(24)))
    #print(str(bin(z^r)[2::].zfill(24)))
    #print(str(bin(o^r)[2::].zfill(24)))

    a = str(bin(d^r)[2::].zfill(24)).count("1")
    b = str(bin(z^r)[2::].zfill(24)).count("1") + 1
    c = str(bin(o^r)[2::].zfill(24)).count("1") + 1
    #print(a,b,c)
    print(min(a,b,c))

    #print(a)
    #print(d^r)
    #print(int("000000000000000001100010",2))
    #print(bin(98)[2::].zfill(24))
    #print(bin(38)[2::].zfill(24))
    #print(bin(68)[2::].zfill(24))
"""
Input:
98 38
5 1048575
0 0
"""
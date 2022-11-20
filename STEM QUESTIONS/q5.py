import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")


pixel = [0,1,2,3,4,5,6,7]
freq = [30,80,20,10,5,89,40,126]
total = sum(freq)

r1 = [1,2]
r2 = [3,7]
r3 = [4,6]
prob = []

def getprob(r):
    range_freq = 0
    for i in range(r[0],r[1]+1):
        range_freq += freq[i]
    prob.append(range_freq/total)

getprob(r1)
getprob(r2)
getprob(r3)

s = sum(prob)
l = len(prob)
print("Average Probability",s/l)

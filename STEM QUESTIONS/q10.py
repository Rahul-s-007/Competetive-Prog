lst = [7,90,87,18,114,90,88,95,87,86,80,20,92,84,17,112,90,84,91,95,80,81,65,91,95,82,20,96,102,116,120,20,99,64,94,82,70,82,95,92,92,90,84,18,114,90,90,71,87,66,65,20,90,65,17,115,65,93]

for key in range(256):
    k = list(bin(key)[2::].zfill(8))
    print("Key=",k)
    print("Message=",end="")
    for c in lst:
        it = list(bin(c)[2::].zfill(8))
        res = ""
        for i in range(8):
            m = int(k[i])
            n = int(it[i])
            res+= str(m^n)
        print(chr(int(res[:8], 2)),end = "")
    print("")


"""
#for i  in lst:
#    print(chr(i) , end = "")

for k in range(257):
    ans = []
    key = bin(k)[2::].zfill(8)
    print("Key:",key)
    print("Message: ",end="")
    for i in lst:
        msg = ""
        bm = bin(i)[2::].zfill(8)
        #print(key,bm)
        for x in range(8):
            res = str(int(bm[x]) ^ int(key[x]))
            msg+=res
        print(chr(int(msg, 2)),end = "")
    print()
"""
"""
def xor_attmpt():
    cipher = []
    for i in lst:
        cipher.append(bin(i)[2::])#add the conversion of the letters/characters
#in your message from ascii to binary withoout the 0b in the front to your ciphered message list
    cipher = "".join(cipher)
    for k in range(256):
        privvyKey = k
        keydecrypt = []
        keydecrypt.append(bin(k)[2::]) #same
        keydecrypt = "".join(keydecrypt )#same

        print("key is '{keydecrypt}'") #substitute values in string
        print(f"encrypted text is '{cipher}'")
        from operator import xor
        for letter in lst:
            print(xor(bool(cipher), bool(keydecrypt)))
xor_attmpt()
"""
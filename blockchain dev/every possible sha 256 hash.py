from hashlib import sha256
for i in range (0,1000000):
    text=str(i)
    tex="90000"
    hash=(sha256((text).encode())).hexdigest()
    hash2=(sha256((tex).encode())).hexdigest()
    print(hash)
    if hash==hash2:
        print("hash has been found and the value of the hash is:",i)
        break
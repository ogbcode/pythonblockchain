from datetime import datetime
from hashlib import sha256
#function to create hash
def hash(data):
        hash_var=sha256((data).encode())
        finalhash=hash_var.hexdigest()
        return finalhash
def sn():
    index=0
    if (index<index+1):
        index+=1
    return index
class Blocks:
    def __init__ (self,transactions,previoushash):
        
        self.transactions=transactions
        self.timestamp=datetime.now()
        self.previoushash=previoushash
        self.blockdata="-".join(transactions)+"-"+previoushash
        self.blockhash=hash(self.blockdata)
        #self.nonce=nonce
        self.time=datetime.now()
         
        print("SN:",sn(),"the block hash is -",self.blockhash,"this block was created at :",self.time)
genesisblock=Blocks("block ne","")
ogb=Blocks("33",genesisblock.blockhash)


t2=Blocks("40",ogb.blockhash)
#print(t2.previoushash)
#print(t2.blockhash)
#print(t2.index)
#print(t2.time)
#ogb.hash()
import json
from hashlib import sha256

def mining(N ,formerhash):
        F1 = open('./Ledgers/Ledger_Number'+str(N)+ '.json')
        B = str(json.load(F1 ))+formerhash
        F2 = open('./Math_Problems/Math_Problem_Number'+str(N)+'.json')
        A = json.load(F2)
        nonce_value = 0
        while 1 :
            D = B + str(nonce_value)
            sha_256 =sha256()
            sha_256.update(D.encode())
            hash=sha_256.hexdigest()
            
            if hash[-4:] == str(A["mathProblem"]):
                print('NUMBER OF BLOCK ---> ' , A["blockNumber"])
                print('HASH OF THE FORMER BLOCK ---> ' , formerhash)                
                print('HASH OF BLOCK ---> ' , hash)
                print('VALUE OF NONCE ---> ' , nonce_value )
                print('')
                return hash
            nonce_value = nonce_value + 1

def genesis():
        F= open('./GenesisBlock/GenesisBlock.json')
        A = str(json.load(F))
        sha256().update(A.encode())
        genesis_hash = sha256().hexdigest()
        print('NUMBER OF BLOCK ---> 1')
        print('HASH OF GENESIS --->' , genesis_hash)
        print('')
        return genesis_hash


former = genesis()
for K in range(2,16):
    hash = mining(K,former )
    former  = hash

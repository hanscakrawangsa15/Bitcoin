import sys
sys.path.append('/Codingan Gabut/Bitcoin')
from Blockchain.Backend.core.EllepticCurve import Sha256Point
from Blockchain.Backend.util.util import hash160
from Blockchain.Backend.util.util import hash256
import secrets

class account:
    def createKeys(self):
        Gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
        Gy = 0x483ada7726a3c4655da4fbfc0e1188a8fd17b448a68554199c47d08ffb10d4b8
    
        G = Sha256Point(Gx,Gy)
        
        privatekey = secrets.randbits(256)
        unCompressesPublicKey = privatekey  *  G
        xpoint = unCompressesPublicKey.x
        ypoint = unCompressesPublicKey.y    
        print(f"Public key is {xpoint},{ypoint}")
        
        if ypoint.num % 2 == 0:
            compressedPublicKey = b'\x02' + xpoint.to_bytes(32,byteorder='big')
        else:
            compressedPublicKey = b'\x03' + xpoint.to_bytes(32,byteorder='big')
        
        hsh160 = hash160(compressedPublicKey)
        main_prefix = b'\x00'
        print(f"Hash160 is {hsh160}")
        newAddress = main_prefix + hsh160
        print(f"Address is {newAddress}")
        
        checkSum = hash256(newAddress)[:4]
        newAddress = newAddress + checkSum
        
        
        count = 0
        
        for c in newAddress:
            if c==0:
                count += 1
            else:
                break
        num = int.from_bytes(newAddress, 'big')
        prefix = '1' *count
        
        result = ' '   
        
        
        
        characters  = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBMN'
        while num > 0:
            num , mod = divmod(num, 58)
            result = characters[mod] + result
            
        PublicAddress= prefix+result
        
if __name__ == "__main__":      
    acc = account()
    acc.createKeys()
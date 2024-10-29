import sys
sys.path.append('/Codingan Gabut/Bitcoin')

from Blockchain.Backend.core.Block import Block
from Blockchain.Backend.core.BlockHeader import BlockHeader
from Blockchain.Backend.util.util import hash256
from Blockchain.Backend.core.database.database import BlockchainDB

ZERO_HASH = '0' * 64
VERSION = 1
import time
import json

class Blockchain:
    def __init__(self):
        self.create_genesis_block()
        
    def write_on_disk(self, block):
        blockchainDB = BlockchainDB()
        blockchainDB.write(block)

    def fetch_last_block(self):
        blockchainDB = BlockchainDB()
        return blockchainDB.lastBlock()

    def create_genesis_block(self):
        blockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(blockHeight, prevBlockHash)
    
    def addBlock (self, blockHeight, prevBlockHash):
        timestamp = int (time.time())
        Transaction = f"Hans sent {blockHeight} Bitcoins to You"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION,prevBlockHash,merkleRoot, timestamp, bits)
        blockheader.mine()
        self.write_on_disk([Block(blockHeight, 1, blockheader.__dict__, 1, Transaction).__dict__])
        
        
    def main(self):
        while True:
            lastBlock = self.fetch_last_block()
            blockHeight = lastBlock['Height'] + 1
            prevBlockHash = lastBlock['Blockheader']['blockhash']
            self.addBlock(blockHeight,prevBlockHash)
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()   
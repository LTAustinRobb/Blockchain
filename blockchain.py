import hashlib
import time
import socket


class Block:
    def __init__(self, index, previoushash, timestamp, data, hash):
        self.index = index
        self.previousHash = previoushash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash





def main():
    def calchash(index, previoushash, timestamp, data):
        val = str(index) + str(previoushash) + str(timestamp) + str(data)
        sha = hashlib.sha256(val.encode('utf-8'))
        return str(sha.hexdigest())

    def calcblockhash(block):
        return calchash(block.index, block.previousHash, block.timestamp, block.data)

    def latestblock():
        return blockchain[len(blockchain) - 1]

    def genesis():
        return Block(0, '0', time.time(), "genesis block", '0')

    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))


    blockchain = [genesis()]

    data = blockchain

    s.send(data)

    blockchain = s.recv()



    def nextblock():
        lastblock = latestblock()
        index = lastblock.index+1
        timestamp = time.time()
        data = "new data"
        hash = calchash(index, lastblock.hash, timestamp, data)
        return Block(index, lastblock.hash, timestamp, data, hash)

    def addblock():
        newblock = nextblock()
        bdata = raw_input("Enter data: ")
        newblock.data = bdata
        blockchain.append(newblock)

    for x in range(0,3):
        addblock()

    for b in blockchain:
        print b.index


if __name__ == '__main__':
    main()






import time
from utils import Hash


class Block():
    def __init__(self, prevHash, height, difficulty, nonce, timestamp, transactions):
        self.hash = None
        self.prevHash = prevHash
        self.height = height
        self.difficulty = difficulty
        self.nonce = nonce
        self.timestamp = timestamp
        self.transactions = transactions

    def B(self):
        return {"hash": self.hash, "prevHash": self.prevHash, "height": self.height, "nonce": self.nonce, "timestamp": self.timestamp, "transactions": self.transactions}

    def mine(self):
        target = "0" * self.difficulty
        h = self.hash
        # TODO: Timer to stop Automatically
        # start_time = time.time()
        while True:
            self.timestamp = int(time.time()*1000)
            h = str(Hash(str(self.B())))

            if h[0:self.difficulty] == target:
                self.hash = h
                break
            b.nonce += 1


if __name__ == "__main__":
    b = Block("hi", 1, 5, 0, 100, ["hi", "hello"])
    print(b.B())
    b.mine()

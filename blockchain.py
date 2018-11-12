import csv

from abc import ABCMeta, abstractmethod

class Blockchain():
    def __init__(self):
        self.blocks = []
        self.latest_block = None

    def new_block(self, block):
        self.blocks.append(block)

    def find_block(self, id):
        return self.blocks[id] #TODO 分岐している場合の処理が必要

    def write_datafile(self, filepath):
        with open(filepath, 'w+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Miner", "Difficulty", "Prev"])
            for block in self.blocks:
                writer.writerow(block.id, block.miner_id, block.difficulty, block.prev_block)
    
  
class Block():
    def __init__(self, id, miner_id, difficulty, prev_block):
        self.id = id
        self.miner = miner_id
        self.difficulty = difficulty
        self.prev_block = prev_block


class Miner():
    def __init__(self, id, hashrate, blockchain, difficulty=1):
        self.id = id
        self.reward = 0
        self.hashrate = hashrate
        self.difficulty = difficulty
        self.blockchain = blockchain

class Consensus(metaclass=ABCMeta):
    @abstractmethod
    def run(self, miners):
        pass
# coding: utf-8

import bitcoin
import fair

# Miner class
class Miner:
    def __init__(self, id, protocol, hashrate):
        self.id = id
        self.reward = 0
        self.consensus = protocol
        self.hashrate = hashrate
        self.difficulty = 1
        self.blockchain = []

    # Simulation Phase 1 function
    # Determine whether node participate in mining or not
    def join_decision(self):
        pass

    # Simulation Phase 2 function
    # If node participate in mining, he execute mining
    def exec_mining(self):
        if self.consensus == "bitcoin":
            return bitcoin.mining(self.hashrate, self.difficulty)
        elif self.consensus == "fair":
            return fair.mining(self.hashrate)

    # Simulation Phase 3 function
    # All nodes finish mining, node select new block
    def select_block(self):
        pass

    def adjust_difficulty(self):
        if self.consensus == "bitcoin":
            self.difficulty = bitcoin.adjust_difficulty(self.difficulty, self.blockchain)
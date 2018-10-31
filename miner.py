# coding: utf-8

import proof_of_work
import fair_proof_of_work

# Miner class
class Miner:
    def __init__(self, id, protocol):
        self.id = id
        self.reward = 0.0
        self.consensus = protocol
        self.hashrate = 0

    # Simulation Phase 1 function
    # Determine whether node participate in mining or not
    def join_decision(self):
        pass

    # Simulation Phase 2 function
    # If node participate in mining, he execute mining
    def exec_mining(self):
        if self.consensus == "proof-of-work":
            proof_of_work.mining(self.hashrate)
        elif self.consensus == "fair-proof-of-work":
            fair_proof_of_work.mining(self.hashrate)

    # Simulation Phase 3 function
    # All nodes finish mining, node select new block
    def select_block(self):
        pass
import csv
import time

import numpy as np

import blockchain

class Simulator():
    def __init__(self, miner_num, eps, protocol):
        self.blockchain = None
        self.miners = []
        self.config = {"num": miner_num, "episode": eps, "protocol": protocol}

    def run(self):
        self.init_simulator(self)

        for _ in range(self.config["episode"]):
            self.phase1()
            self.phase2()
            self.phase3()

        self.end_simulator(self)

    # Initialization of simulation
    @staticmethod
    def init_simulator(self):
        # Initialization of blockchain
        self.blockchain = blockchain.Blockchain()
        # Initialization of miner
        for i in range(self.config["num"]):
            hr = -1
            while hr < 0:
                #TODO この正規分布のパラメータもコンフィグで設定できるようにする
                hr = int(np.random.normal(300000,100000))
            self.miners.append(blockchain.Miner(
                id=i, hashrate=hr, blockchain=self.blockchain))

        # Initialization of data files
        timestamp = str(int(time.time()))
        self.log_filepath = "log/" + self.config.protocol + "_" + timestamp + ".log"
        self.data_filepath = "data/" + self.config.protocol + "_" + timestamp + ".csv"

    @staticmethod
    def phase1():
        pass

    @staticmethod
    def phase2():
        pass
    
    @staticmethod
    def phase3():
        pass

    @staticmethod
    def end_simulator(self):
        self.blockchain.write_datafile(self.data_filepath)
        
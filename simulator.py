import csv
import time
import logging
import logging.config

import numpy as np

import blockchain
import bitcoin
import fair

class Simulator():
    def __init__(self, miner_num, block_num, protocol):
        self.blockchain = None
        self.miners = []
        self.protocol = None
        self.config = {"miner_num": miner_num, "blocks": block_num, "protocol": protocol}

    def run(self):
        self.init_simulator(self)

        for _ in range(self.config["block_num"]):
            self.protocol.run(self.miners)

        self.end_simulator(self)

    # Initialization of simulation
    @staticmethod
    def init_simulator(self):
        # Initialization of blockchain
        self.blockchain = blockchain.Blockchain()

        # Initialization of miner
        for i in range(self.config["miner_num"]):
            hr = -1
            while hr < 0:
                #TODO この正規分布のパラメータもコンフィグで設定できるようにする
                hr = int(np.random.normal(300000,100000))
            self.miners.append(blockchain.Miner(
                id=i, hashrate=hr, blockchain=self.blockchain))

        # Initialization of consensus protocol
        if self.config.protocol == "bitcoin":
            self.protocol = bitcoin.Bitcoin()
        elif self.config.protocol == "fair":
            self.protocol = fair.Fair_PoW()

        # Initialization of data files
        timestamp = str(int(time.time()))
        self.log_filepath = "log/" + self.config.protocol + "_" + timestamp + ".log"
        self.data_filepath = "data/" + self.config.protocol + "_" + timestamp + ".csv"

    @staticmethod
    def end_simulator(self):
        self.blockchain.write_datafile(self.data_filepath)


def main():
    s = Simulator(10,1,"bitcoin")
    s.run()

if __name__ == '__main__':
    main()
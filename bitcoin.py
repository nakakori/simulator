# coding: utf-8

import numpy as np
from scipy.stats import poisson

import blockchain

# Simulation of Proof-of-Work
class Bitcoin(blockchain.Consensus):
    def __init__(self):
        pass

    def run(self, miners):
        self.phase1()
        self.phase2()
        self.phase3()

    # マイニングに参加するかどうかの決定
    # マイナー同士で協力するかどうかをそれぞれで決定
    @staticmethod
    def phase1():
        pass

    # マイニングシミュレーション
    # ブロックの作成・同期
    @staticmethod
    def phase2():
        pass
    
    # 各種パラメータの変動
    # ブロック数が2016毎に難易度を調整(ビットコインの場合)
    # 次のマイニングに参加するかどうかの確率の変更？
    @staticmethod
    def phase3():
        pass

# simulation mining function
def mining(hashrate, difficulty=1):
    # ポアソン分布のパラメータ
    p = 1/(difficulty * 2**32)
    mu = p*hashrate

    # 1秒毎にポアソン分布に従ってトスをする
    # 1ならマイニング成功、0なら失敗
    toss = poisson.rvs(mu, size=3600)
    mining_time = np.where(toss == 1)[0]

    if len(mining_time) == 0:
        result = -1
    else: 
        result = mining_time[0]
    
    return result

# simulation adjust difficulty every 2016 blocks (two weeks)
def adjust_difficulty(current_diff, blockchain):
    latest_blocks = blockchain[len(blockchain)-2016:]
    next_diff = current_diff * (2016 * 600 / sum(latest_blocks))
    if next_diff < 1:
        next_diff = 1
    return next_diff

def success_mining(times):
    ts = sorted(times)
    for t in ts:
        if t != -1:
            return t
    return None
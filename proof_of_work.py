# coding: utf-8

import numpy as np
from scipy.stats import bernoulli
import csv

# Simulation of Proof-of-Work
# Difficulty is length of first 0 bit string
# Bitcoin genesis block's difficulty is 32

max_bit = 256

def mining(hashrate, difficulty=32):
    # Calculate a probability of generating block from hashrate and difficulty 
    p = hashrate / 2**difficulty

    # 二項分布によって条件を満たすハッシュ値を見つけることができるかどうかをシミュレーション
    # 1秒毎にブロック生成が成功したかどうかを計算
    # 3600秒=1時間分の計算をする
    # 一番小さい値をブロック生成が成功した時間とする
    success = bernoulli.rvs(p, size=3600)
    success_index = np.where(success == 1)[0]

    if len(success_index) == 0:
        result = -1
    else: 
        result = success_index[0]
    
    return result

def main():
    miners = [10000, 100000, 300000, 500000, 1000000, 5000000]
    
    for miner in miners:
        results = []
        fail = 0
        for _ in range(100):
            result = mining(miner)
            if result != -1:
                results.append(result)
            else:
                fail += 1
        print("Miner's hashrate:", miner)
        if fail != 100:
            ave = sum(results)/len(results)
            print("Average time: ", int(ave/60), "m", int(ave%60), "s", sep='')
        print("success: ", len(results), ", fail: ", fail, sep='')

if __name__ == '__main__':
    main()
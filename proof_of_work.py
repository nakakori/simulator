# coding: utf-8

import numpy as np
from scipy.stats import poisson
# import csv

# Simulation of Proof-of-Work

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

def test1_pow(miners):
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

def test2_pow(miners):
    bc = []
    diff = 1
    miner_results = [0] * len(miners)

    c = 1
    while c <= 2016:
        result = 0
        times = []
        fail = 0
        for miner in miners:
            times.append(mining(miner,diff))
        result = success_mining(times)
        if result == None:
            fail += 1
            continue
        else:
            miner_results[times.index(result)] += 1
            result += 3600*fail
            # print(c, "回目 : ", int(result/60), "m", int(result%60), "s", sep='')
            c += 1
            bc.append(result)

    print("Average time: ", int(sum(bc)/len(bc)/60), "m", int(sum(bc)/len(bc)%60), "s", sep='')
    print(miner_results)
    print(adjust_difficulty(diff,bc))


def main():
    # miners = [10000, 100000, 300000, 500000, 1000000, 5000000]
    miners = [100000] * 70
    # test1_pow(miners)
    test2_pow(miners)


if __name__ == '__main__':
    main()
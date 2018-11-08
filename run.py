import sys
import argparse
import csv
import time

import numpy as np

import miner
import bitcoin

def get_args():
    parser = argparse.ArgumentParser(
        description="This is the simulator of Blockchain consensus protocol.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-p", "--protocol", 
        help="simulate the specified consensus protocol.", 
        type=str, 
        choices=["bitcoin", "fair"],
        default="bitcoin")
    parser.add_argument("-n", "--number", 
        help="simulate the number of miners.", 
        type=int,
        default=1000)
    parser.add_argument("-e", "--episode",
        help="simulate the number of episode.",
        type=int, 
        default=1)
    parser.add_argument("-m", "--month",
        help="simulate the specified time. Unit is month.",
        type=int, 
        default=12)
    parser.add_argument("-l", "--load",
        help="load simulated log file",
        type=str,
        metavar="DATA_FILE.csv")

    args = parser.parse_args()

    return args

def init_miner(n, p):
    miners = []

    for i in range(n):
        h = -1
        while h < 0:
            h = int(np.random.normal(300000,100000))
        
        miners.append(miner.Miner(i, p, h))
    return miners

def main():
    args = get_args()

    filepass = 'log/' + args.protocol + '_' + str(int(time.time())) + '.csv'
    f = open(filepass, 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(["ID", "Hashrate", "Reward"])

    for _ in range(args.episode):
        miners = init_miner(args.number, args.protocol)
        bc = []
        diff = [1]
        
        for cnt in range(args.month*30*144):
            result = 0
            times = []
            fail = 0
            for miner in miners:
                times.append(miner.exec_mining())

            result = bitcoin.success_mining(times)
            if result == None:
                while result == None:
                    fail += 1
                    times = []
                    for miner in miners:
                        times.append(miner.exec_mining())
                    result = bitcoin.success_mining(times)
            
            miners[times.index(result)].reward += 1
            result += 3600*fail
            bc.append(result)
            
            if cnt !=0 and cnt%2016 == 0:
                for miner in miners:
                    miner.blockchain = bc
                    miner.adjust_difficulty()
                diff.append(miners[0].difficulty)

        print("Average time: ", int(sum(bc)/len(bc)/60), "m", int(sum(bc)/len(bc)%60), "s", sep='')
        print(diff)

        for miner in miners:
            writer.writerow([miner.id, miner.hashrate, miner.reward])

    f.close()

if __name__ == '__main__':
    main()
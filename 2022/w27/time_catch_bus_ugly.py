from typing import List


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses = sorted(buses)
        # print(f'buses: {buses}')
        passengers = sorted(passengers)
        # print(f'passs: {passengers}')
        i = 0
        n_pass = 0
        full = False
        for k, depart in enumerate(buses):
            if k == len(buses) - 1:
                while i < len(passengers) and passengers[i] <= depart:
                    n_pass += 1
                    i += 1
                    if n_pass == capacity:
                        full = True
                        break
            else:
                while i < len(passengers) and passengers[i] <= depart and n_pass < capacity:
                    n_pass += 1
                    i += 1
                n_pass = 0
                # print(f'depart: {depart}')
                # print(f'i: {i}')
        # print(f'full: {full}')
        if not full:
            pass_set = set(passengers)
            for t in range(buses[-1], -1, -1):
                if t not in pass_set:
                    return t
        last = passengers[i - 1]
        # print(f'last: {last}')
        for p in reversed(passengers[:i-1]):
            if last - p > 1:
                break
            last = p
        return last - 1


def test(mine, expected):
    assert mine == expected, f'mine: {mine} vs expected: {expected}'


sol = Solution()
buses = [10,20]
passengers = [2,17,18,19]
capacity = 2
test(sol.latestTimeCatchTheBus(buses, passengers, capacity), 16)

buses = [20,30,10]
passengers = [19,13,26,4,25,11,21]
capacity = 2
test(sol.latestTimeCatchTheBus(buses, passengers, capacity), 20)

buses = [3]
passengers = [2,4]
capacity = 2
test(sol.latestTimeCatchTheBus(buses, passengers, capacity), 3)

buses = [3]
passengers = [2,3]
capacity = 2
test(sol.latestTimeCatchTheBus(buses, passengers, capacity), 1)

buses = [2]
passengers = [2]
capacity = 2
test(sol.latestTimeCatchTheBus(buses, passengers, capacity), 1)

buses = [7,12,15,11,14,13,5,4,2,8,9,19]
passengers = [2,5,10,12,8,19,9,14,4,7,15,13]
capacity = 2
test(sol.latestTimeCatchTheBus(buses, passengers, capacity), 18)

buses = [2241,1239,4280,5025,4354,1749,6310,7993,8163,9369,342,6387,9147,8985,3055,1406,42,8060,1583,5844,5553,119,8043,7836,4159,5512,9230,1220,1893,9411,8319,862,6689,7209,1305,8958,6658,8909,9351,9070,9586,7175,9251,7514,2850,6390,6355,1551,8513,843,8170,4831,6342,8849,2879,8937,2755,5890,7293,1737,4324,2034,7425,9785,1354,6476,3059,6526,8193,9537,2749,8541,5187,8219,369,8467,8140,8175,7287,2598,415,2306,1781,1555,3388,622,7574,4537,4833,1023,4841,7482,6518,4941,9758,7583,1341,5981,6687,6450]
passengers = [8218,5861,7144,1315,9370,846,7541,6688,6348,3526,1343,8043,6326,8697,1738,8306,7292,9506,8537,2827,15,3310,1848,1668,8487,9785,3059,7480,5403,8165,6474,2384,8913,1914,9555,6197,4912,502,646,5837,5940,1366,3012,5074,4254,5545,4841,6520,9138,2877,1252,2755,9039,9359,4832,7185,8889,2653,7576,1512,7863,9712,2102,1239,329,1750,4787,2280,5012,7486,6662,411,6368,8098,6481,1557,8161,8449,1553,9349,9232,4284,24560,72,7276,8045,906,8942,7405,7710,8176,8172,6388,1135,6638,4325,356,9216,8959,4507,6406]
capacity = 5
test(sol.latestTimeCatchTheBus(buses, passengers, capacity), 9784)

from collections import Counter

def count_all_ways(n):
    mem = Counter()
    return _count_all_ways(n, 0, 0, 0, 0, mem)

def _count_all_ways(n, num_25, num_10, num_5, num_1, mem):
    if n < 0:
        return 0
    if n == 0 and not mem[(num_25, num_10, num_5, num_1)]:
        mem[(num_25, num_10, num_5, num_1)] = 1
        return 1

    num_ways = 0
    num_25 += 1
    num_ways += _count_all_ways(n - 25, num_25, num_10, num_5, num_1, mem)
    num_25 -= 1
    num_10 += 1
    num_ways += _count_all_ways(n - 10, num_25, num_10, num_5, num_1, mem)
    num_10 -= 1
    num_5 += 1
    num_ways += _count_all_ways(n - 5, num_25, num_10, num_5, num_1, mem)
    num_5 -= 1
    num_1 += 1
    num_ways += _count_all_ways(n - 1, num_25, num_10, num_5, num_1, mem)
    num_1 -= 1

    return num_ways

def count_all_ways1(n):
    mem = Counter()
    coins = [25, 10, 5, 1]
    return _count_all_ways1(n, coins, mem, 0)

def _count_all_ways1(n, coins, mem, index):
    if mem[(n, index)]:
        return mem[(n, index)]
    if index == len(coins) - 1:
        return 1
    coin = coins[index]
    ways = 0
    i = 0
    while i * coin <= n:
        ways += _count_all_ways1(n - coin * i, coins, mem, index + 1)
        i += 1
    mem[(n, index)] = ways

    return ways

print(count_all_ways(25))
print(count_all_ways1(25))

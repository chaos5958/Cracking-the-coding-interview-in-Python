from collections import Counter

def get_power_set_old(arr):
    power_set = []
    power_set.append(None)
    index = [i for i in range(len(arr))]
    mem = Counter()
    _get_power_set_old(arr, index, power_set, mem)
    return power_set

def _get_power_set_old(arr, indexes, power_set, mem):
    if mem[tuple(indexes)]:
        return

    sub_set = []
    if len(indexes) == 1:
        sub_set.append(arr[indexes[0]])
        mem[tuple(indexes)] = 1
        power_set.append(sub_set)
    else:
        mem[tuple(indexes)] = 1
        for i in range(len(indexes)):
            sub_set.append(arr[indexes[i]])
        power_set.append(sub_set)
        for i in range(len(indexes)):
            index = indexes.pop(i)
            _get_power_set_old(arr, indexes, power_set, mem)
            indexes.insert(i, index)

def get_power_set(nums):
    n = len(nums)
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output

test = [1, 2, 3, 4]
print(len(get_power_set(test)))
print(get_power_set(test))

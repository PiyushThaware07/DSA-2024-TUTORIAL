nums = [1,2,2,3,1]
hashmap = {}
for num in nums:
    if num not in hashmap:
        hashmap[num] = 1
    else:
        hashmap[num] += 1
degree1 = max(sorted(hashmap.values()))


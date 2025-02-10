nums = [1, 2, 2, 3, 1]

count = {}
start = {}
end = {}
maxFrequency = 0

for index, num in enumerate(nums):
    if num not in count:
        count[num] = 1
        start[num] = index
        end[num] = index
    else:
        count[num] += 1
        end[num] = index
    maxFrequency = max(maxFrequency, count[num])

print(count)  # Frequency of each element
print(start)  # Start indices of each element
print(end)    # End indices of each element

result = float('inf')

# Find the smallest subarray length for the element with the highest frequency
for key in count:
    if count[key] == maxFrequency:
        temp = end[key] - start[key] + 1
        result = min(result, temp)

print(result)

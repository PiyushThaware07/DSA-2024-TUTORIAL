s = "abcdefg"
k = 2

temp = ""
result = ""
count = 0
for right in range(len(s)):
    temp += s[right]
    count += 1
    if count == 2 * k:
        result += temp[:k][::-1] + temp[k:]
        temp = ""
        count = 0
if temp:
    if len(temp) < k:
        result += temp[::-1]
    else:
        result += temp[:k][::-1] + temp[k:]
print(result)
# Brute Force
input = [-2,5,-5,0,3,-9]
output = [5,0,3,-2,-5,-9]

positive = []
negative = []
for i in range(0,len(input)):
    # handle negative number
    if input[i]<0:
        negative.append(input[i])
    else:
        positive.append(input[i])
positive.extend(negative)
print(positive)



# Better
input = [-2,5,-5,0,3,-9]
def swap(arr,i,j):
    temp =arr[i]
    arr[i] = arr[j]
    arr[j] = temp

for i in range(0,len(input)):
    for j in range(i+1,len(input)):
        if input[j]>=0 and input[j]>input[i]:
            swap(input,i,j)
            print(input)
            break
print(input)

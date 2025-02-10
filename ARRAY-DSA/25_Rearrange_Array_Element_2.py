'''
TYPE - 2 : Alternating Order
here we have unequal positives and negatives
Ex : 3 positive & 2 negative
'''

def RearrangebySign(A, n):
    # Define 2 lists, one for storing positive 
    # and other for negative elements of the array.
    pos = []
    neg = []
    
    # Segregate the array into positives and negatives.
    for i in range(n):
        if A[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])
    
    # If positives are lesser than the negatives.
    if len(pos) < len(neg):
        # First, fill array alternatively till the point 
        # where positives and negatives are equal in number.
        for i in range(len(pos)):
            A[2*i] = pos[i]
            A[2*i+1] = neg[i]
        
        # Fill the remaining negatives at the end of the array.
        index = len(pos)*2
        for i in range(len(neg)-len(pos)):
            A[index] = neg[len(pos)+i]
            index += 1
    
    # If negatives are lesser than the positives.
    else:
        # First, fill array alternatively till the point 
        # where positives and negatives are equal in number.
        for i in range(len(neg)):
            A[2*i] = pos[i]
            A[2*i+1] = neg[i]
        
        # Fill the remaining positives at the end of the array.
        index = len(neg)*2
        for i in range(len(pos)-len(neg)):
            A[index] = pos[len(neg)+i]
            index += 1
    return A

# Array initialization
n = 6
A = [1, 2, -4, -5, 3, 4]

ans = RearrangebySign(A, n)

for i in range(len(ans)):
    print(ans[i], end=" ")
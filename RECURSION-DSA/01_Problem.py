
# ! Update counter : update counter until it reaches to 5 and once it reaches to 5 it will backtrack to its previous calling function.
def updateCounter(count):
    print(count)
    if count == 5:
        return
    updateCounter(count+1)
updateCounter(0)



# ! Print the name N-times
def getName(N):
    # termination condition
    if N == 0:
        return 
    print("Hello World")
    getName(N-1)
getName(5)

# ! Print numbers linearly from 1 to N
def printNum(N):
    if N == 0:
        return
    printNum(N-1)
    print("Backtracking -> ",N)
printNum(5)


# ! Print numbers linearly from N to 1
def printNum(N):
    if N == 0:
        return
    print("forwarding -> ",N)
    printNum(N-1)
printNum(5)


# ! Print the submission of first N natural number
def submission(N):
    if N == 0:
        return N
    return N + submission(N-1)
print("Submission of first N natural number is -> ",submission(5))


# ! Print the factorial of N
def factorial(N):
    if N == 0 or N == 1:
        return N
    return N * factorial(N-1)
print("Factorial of N is -> ",factorial(5))
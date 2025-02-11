class Solution:
    def generate(self,arr,index,current,result):
        if index >= len(arr):        # Base Case
            result.append(current[::])
            return
        
        current.append(arr[index])   # Take Element
        self.generate(arr,index+1,current,result)

        current.pop()                # Not Take Element
        self.generate(arr,index+1,current,result)


    def brute(self,text1,text2):
        arr1 = list(text1)
        sub1 = []
        self.generate(arr1,0,[],result=sub1)
        
        arr2 = list(text2)
        sub2 = []
        self.generate(arr2,0,[],result=sub2)

        longest = 0
        for i in sub1:
            for j in sub2:
                if i == j and longest < len(i):
                    longest = max(longest,len(i))
        print(longest)




    def isLongest(self,text1,text2,i,j):
        # base case
        if i == len(text1) or j == len(text2):
            return 0
        
        longest = 0
        if text1[i] == text2[j]:
            longest = 1 + self.isLongest(text1,text2,i+1,j+1)
        else:
            longest = max(
            self.isLongest(text1,text2,i+1,j) 
            ,
            self.isLongest(text1,text2,i,j+1)
            )
        return longest
    
    def better(self,text1,text2):
        result = self.isLongest(text1,text2,0,0)
        print(result)

    
    def optimize(self,text1,text2):
        n = len(text1)
        m = len(text2)
        dp = np.zeros((n+1, m+1))

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1   # set digonal value
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        print(int(dp[n][m]))



text1 = "abcde"
text2 = "abe" 
s = Solution()
# s.brute(text1,text2)
# s.better(text1,text2)
s.optimize(text1,text2)
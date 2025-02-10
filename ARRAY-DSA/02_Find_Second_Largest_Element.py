'''
Find the second largest element in an array
1. Better Solution
    * Find the largest element:
        Iterate through the array to find the largest element (largestElement).
    * Find the second largest element:
        Iterate through the array again and compare each element:
    * If an element is greater than the current sLargestElement and less than largestElement, update sLargestElement.
    * Print the second largest element.

2. Optimal Solution
    * Initialize largestElement with the first element of the array and sLargestElement with -1.
    * Iterate through the array:
        If the current element is greater than largestElement:
            Update sLargestElement to the current largestElement.
            Update largestElement to the current element.
        Otherwise, if the current element is less than largestElement but greater than sLargestElement:
            Update sLargestElement.
    * Print the second largest element.

Example 1 : [1,2,3,4,5] 
--> In this example as there is no repetation of number so the second largest will be n-2

Example 2 : [1,2,3,4,4,5,5]
--> In this example as the numbers are repeating so the n-2 => 5 it is not the second largest the second largest must be unique so what we can do we can start iteration from n-2 check it with the largest if it is not equal then that was the second largest element of an array.
'''

class Solution:
    def brute(self,arr):
        n = len(arr)
        # Insertion Sort
        for i in range(n):
            temp = arr[i]
            prev = i-1
            while(prev>=0 and arr[prev]>temp ):
                arr[prev+1] = arr[prev]
                prev = prev-1
            arr[prev+1]= temp
        # Second Largest
        largest = arr[n-1]
        for i in range(n-2,-1,-1):
            if arr[i] != largest:
                print(arr[i])
                return 
            
    
    def better(self,arr):
        # pass-1 : find the largest element of an array
        n = len(arr)
        largest = arr[0]
        for i in range(1,n):
            if arr[i]>largest:
                largest = arr[i]
        
        # pass - 2 : again iterate the entire array by secondLargest as -1 and update its value if the following conditions matches
        secondLargest = -1
        for i in range(0,n):
            if arr[i]>secondLargest and arr[i] != largest:
                secondLargest = arr[i] 
        print(secondLargest)
        return
    

    def optimial(self,arr):
        # suppose you have 2 no 1,2 here suppose 1 is largest and you had compre it with 2 , hey 2 are you greate than me 2 says yes i am so 1 will be the secondLargest here while 2 will be the lagrest element
        n = len(arr)
        largest = arr[0]
        slargest = -1
        for i in range(1,n):
            if arr[i]>largest:
                slargest = largest
                largest = arr[i]
            if arr[i]<largest and arr[i]>slargest:
                slargest = arr[i]
        print(slargest)
        return

            


nums = [54,2,34,1,67,55,55,67,67,4]
s = Solution()
s.brute(nums)
s.better(nums)
s.optimial(nums)



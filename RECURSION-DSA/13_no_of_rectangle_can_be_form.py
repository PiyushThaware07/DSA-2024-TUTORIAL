class Solution:
    def countGoodRectangles(self, rectangles):
        hashmap = {}
        for length, weight in rectangles:
            side = min(length, weight)
            if side not in hashmap:
                hashmap[side] = 1
            else:
                hashmap[side] += 1
        largest = max(hashmap.keys())
        print(hashmap[largest]) 


sol = Solution()
sol.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]])
sol.countGoodRectangles([[2,3],[3,7],[4,3],[3,7]])
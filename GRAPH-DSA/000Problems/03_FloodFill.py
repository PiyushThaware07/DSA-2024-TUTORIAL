class Solution:
    def flood_fill(self, image, starting, ending, newColor):
        # 1. Determine the number of rows and columns in the image matrix
        rows = len(image)
        cols = len(image[0])
        
        # 2. Get the original color of the starting pixel
        originalColor = image[starting][ending]
        
        # 3. If the original color is the same as the new color, no need to proceed
        if newColor == originalColor:
            return image
        
        # 4. Set the starting point in the image to the new color
        image[starting][ending] = newColor
        queue = [(starting, ending)]
        
        # 5. Perform flood fill using DFS
        while queue:
            row, col = queue.pop(0)
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for i,j in directions:
                if 0 <= i < rows and 0<= j < cols and image[i][j] == originalColor:
                    image[i][j] = newColor
                    queue.append((i,j))
        return image


# Test the code
image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
start = 1
end = 1
color = 2

sol = Solution()
result = sol.flood_fill(image, starting=start, ending=end, newColor=color)
print(result)

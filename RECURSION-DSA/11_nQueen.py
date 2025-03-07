class Solution:
    def print_board(self, board):
        for row in board:
            print(" ".join(row))
        print()  # For spacing between solutions

    def is_safe(self, board, row, col, n):
        # Check vertical column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check upper-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True  # Position is safe

    def solve_nqueens(self, board, row, n):
        if row == n:
            self.print_board(board)  # Print solution
            return
        
        for col in range(n):
            if self.is_safe(board, row, col, n):
                board[row][col] = "Q"  # Place queen
                self.solve_nqueens(board, row + 1, n)  # Recur for next row
                board[row][col] = "."  # Backtrack

    def nQueen(self, n):
        board = [["." for _ in range(n)] for _ in range(n)]  # Initialize board
        self.solve_nqueens(board, 0, n)  # Start solving from row 0

# Example Usage
sol = Solution()
sol.nQueen(4) 

import collections

# O(1) time, O(1) space
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)

        # validate rows
        for i in range(n):
            nums = [num for num in board[i] if num.isdigit()]
            if len(set(nums)) != len(nums):
                return False

        # validate columns
        for i in range(n):
            nums = []
            for j in range(n):
                if board[j][i].isdigit():
                    nums.append(board[j][i])
            if len(set(nums)) != len(nums):
                return False
        
        # validate boxes
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                nums = []
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        if board[row][col].isdigit():
                            nums.append(board[row][col])
                if len(set(nums)) != len(nums):
                    return False

        return True

# O(1) time, O(1) space
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for row in range(n):
            for col in range(n):
                num = board[row][col]
                if num == ".":
                    continue
                if (num in rows[row] or num in cols[col] or num in boxes[(row // 3, col // 3)]):
                    return False
                cols[col].add(num)
                rows[row].add(num)
                boxes[(row // 3, col // 3)].add(num)

        return True

# valid board
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))

# invalid row
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".","6",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))

# invalid column
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))

# invalid box
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".","6",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))
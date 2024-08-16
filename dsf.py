from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])


        for r in range(rows):
            val = matrix[r][0]
            i, j = r, 0
            while i < rows and j < cols:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1


        for c in range(1, cols):
            val = matrix[0][c]
            i, j = 0, c
            while i < rows and j < cols:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1

        return True


matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
my_list = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]

solution = Solution()


if solution.isToeplitzMatrix(matrix):
    print("true")
else:
    print("false")


if matrix == my_list:
    print("оно правильное")
else:
    print("оно неправильное")

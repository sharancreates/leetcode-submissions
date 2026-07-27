class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r = len(mat)      
        c = len(mat[0])  

        count = 0

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    if self.checkSpl(i, j, r, c, mat):
                        count += 1

        return count

    def checkSpl(self, i, j, r, c, mat):
        for col in range(c):
            if col != j and mat[i][col] == 1:
                return False

        for row in range(r):
            if row != i and mat[row][j] == 1:
                return False

        return True
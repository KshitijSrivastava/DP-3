## Problem2 (https://leetcode.com/problems/minimum-falling-path-sum/)


class Solution:
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        nrows = len(matrix)
        ncols = len(matrix[0])
        dp = {}
        
        def minFallingPathSum_recur(matrix, i, j):
            if i == nrows:                              #if it reaches crosses the last row
                return 0
            elif j < 0 or j >= nrows:                   #if it crosses the left and right 
                return float('inf')
            elif (i, j) in dp:                          #if found in the hash map
                return dp[ (i,j) ]
            
            min_array = []
            
            if i == 0:                                  #go sideways when in row 0
                value1 = minFallingPathSum_recur(matrix, i, j+1 )
                min_array.append(value1)
                
            
            for dx, dy in [ (1, -1), (1, 0), (1, 1) ]:#Try all possible combinations from a point
                value = matrix[i][j] + minFallingPathSum_recur(matrix, i + dx, j + dy)
                min_array.append(value)
                
            dp[ (i,j) ] = min(min_array) # Find the minimum and store it in the dp
            return dp[ (i,j) ]          #return the value
        
        return minFallingPathSum_recur(matrix, i = 0, j = 0)
                
            
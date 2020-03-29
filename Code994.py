class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        # Solution 1
        # minute = 0
        # rowCount = len(grid)
        # colCount = len(grid[0])
        # while True:
        #     hasfresh = False
        #     infected = [] 
        #     for row_index in range(0, rowCount):
        #         for col_index in range(0, colCount):
        #             if grid[row_index][col_index] == 1:
        #                 hasfresh = True
        #             if grid[row_index][col_index] == 2:
        #                 if row_index > 0 and grid[row_index - 1][col_index] == 1:
        #                     infected.append([row_index - 1, col_index])
        #                 if row_index < rowCount - 1 and grid[row_index + 1][col_index] == 1:
        #                     infected.append([row_index + 1, col_index])
        #                 if col_index > 0 and grid[row_index][col_index - 1] == 1:
        #                     infected.append([row_index, col_index - 1])
        #                 if col_index < colCount - 1 and grid[row_index][col_index + 1] == 1:
        #                     infected.append([row_index, col_index + 1])

        #     if len(infected) > 0 and hasfresh:
        #         for location in infected:
        #             grid[location[0]][location[1]] = 2
        #         minute = minute + 1
        #     else:
        #         return -1 if hasfresh else minute

        # Solution 2
        rowCount = len(grid)
        colCount = len(grid[0])
        badOrangeLocations = []
        goodOrangeCount = 0
        for row_index in range(0, rowCount):
            for col_index in range(0, colCount):
                if grid[row_index][col_index] == 2:
                    badOrangeLocations.append([row_index, col_index])
                elif grid[row_index][col_index] == 1:
                    goodOrangeCount = goodOrangeCount + 1
        minite = 0
        while len(badOrangeLocations) > 0 and goodOrangeCount > 0:
            newInfectedLocations = []
            while len(badOrangeLocations) > 0:
                location = badOrangeLocations.pop(0)
                row_index = location[0]
                col_index = location[1]
                if row_index > 0 and grid[row_index - 1][col_index] == 1:
                    grid[row_index - 1][col_index] = 2
                    newInfectedLocations.append([row_index - 1, col_index])
                if row_index < rowCount - 1 and grid[row_index + 1][col_index] == 1:
                    grid[row_index + 1][col_index] = 2
                    newInfectedLocations.append([row_index + 1, col_index])
                if col_index > 0 and grid[row_index][col_index - 1] == 1:
                    grid[row_index][col_index - 1] = 2
                    newInfectedLocations.append([row_index, col_index - 1])
                if col_index < colCount - 1 and grid[row_index][col_index + 1] == 1:
                    grid[row_index][col_index + 1] = 2
                    newInfectedLocations.append([row_index, col_index + 1])
            goodOrangeCount = goodOrangeCount - len(newInfectedLocations)
            badOrangeLocations = newInfectedLocations
            minite = minite + 1

        if goodOrangeCount > 0:
            return -1
        else:
            return minite


print("result = " + str(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])))
print("result = " + str(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]])))
print("result = " + str(Solution().orangesRotting([[0,2]])))
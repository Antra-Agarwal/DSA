class Solution(object):
    def countUnguarded(self, m, n, guards, walls):

        # 0 = empty, 1 = guard, 2 = wall, 3 = guarded
        grid = []
        for x in range(m):
            grid.append([0] * n)

        for i, j in guards:
            grid[i][j] = 1

        for i, j in walls:
            grid[i][j] = 2

       
        for i in range(m):
            guard_seen = False
            for j in range(n):  
                if grid[i][j] == 1:
                    guard_seen = True
                elif grid[i][j] == 2:
                    guard_seen = False
                elif guard_seen:
                    grid[i][j] = 3

            guard_seen = False
            for j in range(n-1, -1, -1): 
                if grid[i][j] == 1:
                    guard_seen = True
                elif grid[i][j] == 2:
                    guard_seen = False
                elif guard_seen:
                    grid[i][j] = 3

       
        for j in range(n):
            guard_seen = False
            for i in range(m): 
                if grid[i][j] == 1:
                    guard_seen = True
                elif grid[i][j] == 2:
                    guard_seen = False
                elif guard_seen:
                    grid[i][j] = 3

            guard_seen = False
            for i in range(m-1, -1, -1):  
                if grid[i][j] == 1:
                    guard_seen = True
                elif grid[i][j] == 2:
                    guard_seen = False
                elif guard_seen:
                    grid[i][j] = 3

       
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1

        return count


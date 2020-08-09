class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rotten = 0
        fresh = 0

        time = 0
        rotten_coords = []

        for y, row in enumerate(grid):
            for x, spot in enumerate(row):
                if spot == 1:
                    fresh += 1
                elif spot == 2:
                    rotten += 1
                    rotten_coords.append([x, y])
                
        while rotten_coords:
            time += 1
            for i in range(0, len(rotten_coords)):
                coords = rotten_coords.pop(0)
                x = coords[0]
                y = coords[1]
                
                if x != 0:
                    if grid[y][x-1] == 1:
                        rotten_coords.append([x-1, y])
                        grid[y][x-1] = 2
                        fresh -= 1 

                if x < len(grid[0])-1:
                    if grid[y][x+1] == 1:
                        rotten_coords.append([x+1, y])
                        grid[y][x+1] = 2
                        fresh -= 1 

                if y != 0:
                    if grid[y-1][x] == 1:
                        rotten_coords.append([x, y-1])
                        grid[y-1][x] = 2
                        fresh -= 1 

                if y < len(grid)-1:
                    if grid[y+1][x] == 1:
                        rotten_coords.append([x, y+1])
                        grid[y+1][x] = 2
                        fresh -= 1 

        if fresh != 0:
            return -1

        return max(0, time-1)

            
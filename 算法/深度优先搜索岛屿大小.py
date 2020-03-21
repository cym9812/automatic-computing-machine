def maxAreaOfIsland(grid) -> int:
    ans = 0
    for i, l in enumerate(grid):
        for j, n in enumerate(l):
            cur = 0
            stack = [(i, j)]
            while stack:
                cur_i, cur_j = stack.pop()
                if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                    continue
                cur += 1
                grid[cur_i][cur_j] = 0
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    next_i, next_j = cur_i + di, cur_j + dj
                    stack.append((next_i, next_j))
            ans = max(ans, cur)
    return ans
print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))

def maxAreaOfIsland1(grid) -> int:
    ans = 0
    i_lim = len(grid)
    j_lim = len(grid[0])
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    for i, m in enumerate(grid):
        for j, n in enumerate(m):
            stack = [[i,j]]
            curr = 0
            while stack:
                curr_i, curr_j = stack.pop()
                if 0 <= curr_i < i_lim and 0 <= curr_j < j_lim and grid[curr_i][curr_j] == 1:
                    grid[curr_i][curr_j] = 0
                    curr += 1
                    for di, dj in move:
                        stack.append([curr_i + di,curr_j+dj])
                else:
                     continue
            ans = max(ans, curr)
    return  ans
print(maxAreaOfIsland1([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))

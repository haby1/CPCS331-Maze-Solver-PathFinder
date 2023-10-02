import tkinter as tk
import time


# DFS algorithm
# the final path using DFS will be in red color
def dfs(maze, start, end):
    stack = [start]
    visited = set()

    while stack:
        x, y = stack.pop()
        if (x, y) == end:
            return True

        if (x, y) not in visited:
            visited.add((x, y))
            canvas.create_rectangle(y * 25, x * 25, (y + 1) * 25, (x + 1) * 25, fill="red")
            root.update()
            time.sleep(0.05)  # Slow it down so you can see the progress

        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:  # up, right, down, left (clockwise)
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(maze)) and (0 <= ny < len(maze[0])) and (maze[nx][ny] != 1) and ((nx, ny) not in visited):
                stack.append((nx, ny))

    return False


# BFS algorithm
# the final path using BFS will be in blue color
def bfs(maze, start, end):
    queue = [start]
    visited = set()

    while queue:
        x, y = queue.pop(0)
        if (x, y) == end:
            return True

        if (x, y) not in visited:
            visited.add((x, y))
            canvas.create_rectangle(y * 25, x * 25, (y + 1) * 25, (x + 1) * 25, fill="blue")
            root.update()
            time.sleep(0.05)  # Slow it down so you can see the progress

        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:  # up, right, down, left (clockwise)
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(maze)) and (0 <= ny < len(maze[0])) and (maze[nx][ny] != 1) and ((nx, ny) not in visited):
                queue.append((nx, ny))

    return False



# Draw the initial state of the maze
def draw_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            color = "white"
            if maze[i][j] == 1:
                color = "black"
            elif maze[i][j] == 2:
                color = "red"
            elif maze[i][j] == 3:
                color = "green"
            canvas.create_rectangle(j * 25, i * 25, (j + 1) * 25, (i + 1) * 25, fill=color)


# Your maze definition should go here
maze = \
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# The start and end coordinates are in (row, column) format
start = (17, 1)
end = (1, 17)

# Create the tkinter canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=len(maze[0]) * 25, height=len(maze) * 25)
canvas.pack()

# Draw the initial state of the maze
draw_maze(maze)

# Call the DFS and BFS functions here:
dfs(maze, start, end)
bfs(maze, start, end)

root.mainloop()
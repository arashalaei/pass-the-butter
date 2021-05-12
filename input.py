""" 
    @author Arash Alaei <arashalaei22@gmail.com>.
    @since 5/12/2021
"""

import os
import numpy as np

def get_maze(address: str) -> np.ndarray:
    a_file = open(f"./test/{address}.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    
    del lines[0]

    new_file = open("./test/tmp.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

    maze = np.loadtxt(f"./test/tmp.txt", dtype=str)

    os.remove("./test/tmp.txt")

    return maze

def get_positions(maze: np.ndarray) -> tuple:
    r_pos = None
    b_pos = []
    p_pos = []

    for row in range(maze.shape[0]):
        for col in range(maze.shape[1]):
            if 'r' in maze[row][col]:
                r_pos = (row, col)
            elif 'b' in maze[row][col]:
                b_pos.append((row, col))
            elif 'p' in maze[row][col]:
                p_pos.append((row, col))
    return r_pos, b_pos, p_pos
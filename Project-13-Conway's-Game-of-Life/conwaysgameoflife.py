#!/usr/bin/env python
""" Conway's Game of life, by Al Sweigart al@inventwithpython.com
The classic cellular automota simulation. Press Ctrl-C to stop.
More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
View this code at: https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, simulation """

import copy, random, sys, time

# Setup the constants
WIDTH = 150   # Width of the cell grid
HEIGHT = 50  # Height of the cell grid

# (!) Try changing ALIVE to '#' or another character
ALIVE='0' # represents a living cell
# (!) Try changing DEAD to '.' or another character
DEAD = ' '

# (!) Try changing ALIVE to '|' and DEAD to '-'

# The cells and nextCells are dictionaries for the state of the game.
# Their keys are (x,y) tuples adn their values are one of teh ALIVE or DEAD values
nextCells = {}
# Put random dead adn alive cells into nextCells:
for x in range(WIDTH): # loop over every possible column
    for y in range(HEIGHT): # Loop over every possible row
        # 50/50 chance for staring cells being alive or dead
        if random.randint(0,1) == 0:
            nextCells[(x,y)] = ALIVE # add a living cell
        else:
            nextCells[(x,y)] = DEAD  # add a dead cell

while True: # Main program loop
    # Each iteration of this loop is a step of the simulation

    print('\n' *50)  # Separate each step with newlines
    cells = copy.deepcopy(nextCells)

    # Print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)], end='') # print # or space
        print() # newline at end of row
    print('Press Ctrl-C to quit')

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates of (x,y) even if they
            # wrap around the edge:
            left  = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y +1 ) % HEIGHT

            # Count the number of living neighbors
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1   # Top-left neighbor is alive
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1 # Top neighbor is alive
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1   # Top-right neighbor is alive
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1 # Left neighbor is alive
            if cells[(right,y)] == ALIVE:
                numNeighbors += 1 # Right neighbor is alive
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1 # Bottom-left neighbor is alive
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1 # Bottom neighbor is alive
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1 # Bottom-right neighbor is alive

            # Set cell based on Conway's game of life rules:
            if cells[(x,y)] == ALIVE and (numNeighbors == 2
                or numNeighbors == 3):
                    # Living cells with 2 or 3 neighbors stay alive:
                    nextCells[(x,y)] = ALIVE
            elif cells[(x,y)] == DEAD and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[(x,y)] = ALIVE
            else:
                # Everything else dies or stays dead:
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1)  # Add a 1 second pause to reduce flickering
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print("By Al Sweigart al@inventwithpython.com")
        sys.exit() # when Ctrl-C is pressed, end the program.
#File Name: GameOfLife.py
#Date: 2019/08/23
#John Conway's Game of Life
#Language: Python using Pygame
#By Justin Snider

#import libaries
import pygame as pg
import numpy as np
import sys
import random #import libaries


def main():
    pg.init() #start library module
    pg.display.set_caption("Game of Life")
    #Initial Variables
    screen_width=640
    screen_height=360
    size = width, height = screen_width, screen_height #set screen size
    cells_live = 0, 200, 0 #rgb color of live cells
    cells_dead = 0, 0, 0 #rgb color of dead cells
    screen_color = 0, 0, 0
    cell_size = 5 #size of cells
    columns = int(screen_width/cell_size)
    rows = int(screen_height/cell_size)
    start_bias = 50 #percentage probability of a cell starting alive
    timer_interval = 250
    move_event = pg.USEREVENT+1
    pg.time.set_timer(move_event, timer_interval)

    #paused = False
    #line_width = 48
    screen = pg.display.set_mode(size) # initialize a window for display

    rand_array = np.random.random((columns,rows))
    arr_cells = np.zeros((columns,rows))
    arr_cells_buf = np.zeros((columns,rows))
    #arr_cell_buffer = np.zeros((rows,columns))
    for x in range(columns):
        for y in range(rows):
            if rand_array[x,y]*100 > start_bias:
                arr_cells[x,y] = 0
            else:
                arr_cells[x,y] = 1

    while True:
        for event in pg.event.get(): # get the events from the queue
            if event.type == pg.QUIT: sys.exit() # if event is quit then exit
            if event.type == move_event:
                #update cells
                #put cells in buffer
                for x in range(columns):
                    for y in range(rows):
                        arr_cells_buf[x,y] = arr_cells[x,y]
                #evaluate each cell
                for x in range(columns):
                    for y in range(rows):
                        #check up
                        count = 0
                        if y+1 < rows:
                            if arr_cells_buf[x,y+1] == 1:
                                count +=1
                            if x+1 < columns:
                                if arr_cells_buf[x+1,y+1] == 1:
                                    count +=1
                            if x-1 >= 0:
                                if arr_cells_buf[x-1,y+1] == 1:
                                    count +=1
                        #check right
                        if x+1 < columns:
                            if arr_cells_buf[x+1,y] == 1:
                                count +=1
                        #check down
                        if y-1 >= 0:
                            if arr_cells_buf[x,y-1] == 1:
                                count +=1
                            if x+1 < columns:
                                if arr_cells_buf[x+1,y-1] == 1:
                                    count +=1
                            if x-1 >= 0:
                                if arr_cells_buf[x-1,y-1] == 1:
                                    count +=1
                        #check left
                        if x-1 >= 0:
                            if arr_cells_buf[x-1,y] == 1:
                                count +=1
                        #check all neighbours and count them
                        #if 2 or 3 neighbours keep alive else kill
                        if arr_cells_buf[x,y] == 1:
                            if count < 2 or count > 3:
                                arr_cells[x,y] = 0
                        else:
                            if count == 3:
                                arr_cells[x,y] = 1

        screen.fill(screen_color)
        for x in range(columns):
            for y in range(rows):
                rec = ((x * cell_size), (y * cell_size), (cell_size), (cell_size))
                if arr_cells[x,y] == 1: #set fill to alive
                    pg.draw.rect(screen,cells_live,rec, 0)
                else: #set fill to dead
                    pg.draw.rect(screen,cells_dead,rec, 0)
        pg.display.update()

main()

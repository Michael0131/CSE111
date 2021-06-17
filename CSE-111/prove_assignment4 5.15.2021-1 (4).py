import tkinter as tk

#call tkinter tk

import math
from tkinter import Tk, Frame, Canvas, BOTH
import random


def main():

    # create root
    width = 800
    height = 600

    #create root Tk
    root = Tk()
    root.geometry(f"{width}x{height}")

    # create a frame
    frame = Frame()
    frame.master.title("scene")
    frame.pack(fill=BOTH, expand=1)

    # create a canvas object that will draw into the frame
    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)
    #call teh draw_scene
    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    draw_background(canvas, scene_left, scene_right, scene_top, scene_bottom)
    draw_sun(canvas, 50, 50)
    draw_mountain(canvas, 200, 700, 400)
    draw_clouds(canvas, scene_top, scene_left, scene_bottom, scene_right, 8)
    draw_grass(canvas, scene_top, scene_left, scene_bottom, scene_right)

    draw_tree(canvas, 500, 150, 40, 60)
    draw_shore(canvas, 400, 360, 400, 100)
    draw_lake(canvas, 400, 350, 400, 100)
    draw_grid(canvas, scene_left, scene_right, scene_top, scene_bottom, 100)
    pass

# draw grid

def draw_grid(canvas, scene_left, scene_right, scene_top, scene_bottom, spacing):
    # horizontal lines
    for i in range(scene_top, scene_bottom, spacing):
        canvas.create_line(scene_left, i, scene_right, i)

    for i in range(scene_left, scene_right, spacing):
        canvas.create_line(i, scene_top, i, scene_bottom)

# make the background

def draw_background(canvas, scene_left, scene_right, scene_top, scene_bottom):
    horizon_line = scene_bottom - (math.ceil(scene_bottom / 2)-100)
    sky_top_left = scene_left, scene_top
    sky_bottom_right = scene_right, horizon_line
    valley = scene_bottom - math.ceil(scene_bottom / 4) - 50
    sky_bottom_left = scene_left, horizon_line
    scene_bottom_right =  scene_right, scene_bottom

    #create

    canvas.create_rectangle(sky_top_left, sky_bottom_right, width = False, fill = "royalBlue1")
    canvas.create_rectangle(sky_bottom_left, scene_bottom_right, width = False, fill = "mediumseagreen")

#Make a sun
def draw_sun(canvas, sun_left, sun_top):
    sun_height = 150
    sun_width = 150
    ray_length = 120
    ray_count = 20

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_y = sun_left + (sun_width / 2)
    sun_center_x = sun_top + (sun_height / 2)

    canvas.create_oval(sun_top, sun_left, sun_bottom, sun_right, fill = "#FFF784", width = False)
    
    # make the sun rays
    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width= 3, fill = "#FFF784")

def draw_mountain(canvas, left, right, bottom):
    top = 500,100
    bottom_left = left, bottom
    bottom_right = right, bottom
    top_2 = 700,50
    bottom_left_2 = left + 100, bottom
    bottom_right_2= right + 100, bottom


    canvas.create_polygon(top, bottom_left, bottom_right, fill = "dimgray")
    canvas.create_polygon(top_2, bottom_left_2, bottom_right_2, fill = "grey")

def draw_tree(canvas, bottom, left, width, height):
    trunk =  left, bottom - height, left + width, bottom + height
    tree_top = left + width/2, bottom - 4*height
    canvas.create_polygon(tree_top, left - 75, bottom - height, left + width + 75, bottom - height, fill = "darkgreen")
    canvas.create_rectangle(trunk, fill = "peru")

def draw_lake(canvas, left, bottom, width, height):
    canvas.create_arc(left, bottom, left + width, bottom + height, start = 0, extent = -180, style = tk.CHORD, fill = "deepskyblue")

def draw_shore(canvas, left, bottom, width, height):
    canvas.create_arc(left, bottom, left + width, bottom + height, start = 0, extent = -193, style = tk.CHORD, fill = "khaki")

def draw_grass(canvas, scene_top, scene_left, scene_bottom, scene_right):
    horizon_line = scene_bottom - 150
    land = scene_bottom 
    grass_length = 25
    grass_height = 15
    grass_amount = 250
    
    for i in range(grass_amount):
        grass_x = scene_left + int(random.randrange(20,scene_right,5))
        grass_y = int(random.randrange(horizon_line, land, 10))

        ######

        arc_left = grass_x, grass_y, grass_x - grass_length, grass_y + grass_height
        arc_right = grass_x, grass_y, grass_x + grass_length, grass_y + grass_height
        canvas.create_arc(arc_left, start = 0, extent = 90, style=tk.ARC)
        canvas.create_arc(arc_right, start = -90, extent = 0, style=tk.ARC)
# Add Clouds

def draw_clouds(canvas, scene_top, scene_left, scene_bottom, scene_right, amount):

    bottom = scene_bottom - (math.ceil(scene_bottom / 2))
    top = scene_top + 150
    left = scene_left + 250
    right = scene_right -100

    # put it where you want

    for _ in range(amount):
        cloud_x = random.randrange(left, right, 20)
        cloud_y = random.randrange(top, bottom, 20)
        cloud_size = random.randint(7,12)

        for _ in range(cloud_size):
            pos = random.randrange(-1,1)
            cloud_size_x= cloud_x + 75 + pos * int(random.randrange(200,300,20))
            cloud_size_y= cloud_y + 25 + pos * int(random.randrange(50,100,10))
            canvas.create_oval(cloud_x, cloud_y, cloud_size_x, cloud_size_y, width = False, fill = "gray93")

main()



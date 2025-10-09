"""
CLI entry point for the gravity simulation.

Usage:
    python main.py <scenario_name> <num_gens> <time_step> <canvas_width> <drawing_frequency>

Example:
    python main.py jupiterMoons 2000 0.01 800 5

This will read:   data/jupiterMoons.txt
and write video:  output/jupiterMoons.mp4
"""

import sys
import os
import time
import pygame
import imageio
from custom_io import read_universe
from gravity import simulate_gravity
from drawing import animate_system, pygame_surface_to_numpy, draw_to_canvas, save_video_from_surfaces

def main():
    """
    Run the full pipeline:
      1) read universe from file
      2) simulate gravity for N generations
      3) render selected frames to pygame surfaces
      4) encode frames to an MP4 video
    """
    print("Let's simulate gravity!")
    
    if len(sys.argv) != 6:
        raise ValueError("Error: incorrect number of parameters.")
    
    scenario = sys.argv[1]

    input_file = f"data/{scenario}.txt"
    input_file = f"output/{scenario}.mp4"

    initial_universe = read_universe(input_file)

    time_points = simulate_gravity(initial_universe,num_gens,time_step)

    canvas_width = 15000
    u = read_universe("data/butterfly.txt")
    

if __name__ == "__main__":
    main()
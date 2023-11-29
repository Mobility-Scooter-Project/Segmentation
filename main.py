'''
Main File
-Handles command line inputs/arguments.
-Pieces together functions from other files.
-Will use the machine's GPU if CUDA is available.
'''

import argparse
import importlib
import torch

# Set up the argument parser
parser = argparse.ArgumentParser(
    prog="Segmentation",
    description="Process videos using bounding box and segmentation models."
)
parser.add_argument('-i', '--input', required=True)
parser.add_argument('o', '--output', required=True)

args = parser.parse_args()

# Check for GPU, and initialize GPU using cuda command
if torch.cuda.device_count() > 0:
    print("GPU is compatible with CUDA.")
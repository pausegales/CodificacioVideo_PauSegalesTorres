import os
import subprocess
import json


def convert_to_mp2(filename):
    """
    Convert the video to MP2 format using FFmpeg.
    """
    os.system(f'ffmpeg -i {filename} BBB_mpg.mpg')
    os.system(f'ffmpeg -i {filename}')


def resize_input(filename):
    """
    Resize the video based on user input for width and height.
    """
    w = int(input("Enter VIDEO WIDTH value: "))
    h = int(input("Enter VIDEO HEIGHT value: "))
    os.system(f'ffmpeg -i {filename} -s {w}x{h} -c:a copy BBB_resized.mp4')


def change_chroma_sub(filename):
    """
    Change the chroma subsampling of the video based on user input.
    """
    a = int(input("Enter 1st parameter of the X:X:X: "))
    b = int(input("Enter 2nd parameter of the X:X:X: "))
    c = int(input("Enter 3rd parameter of the X:X:X: "))
    os.system(f'ffmpeg -i {filename} -c:v libx264 -vf format=yuv{a}{b}{c}p -c:a copy BBB_chroma.mp4')


def get_video_info(filename):
    """
    Get video information (width, height, duration, codec, bitrate) using FFprobe.
    """
    try:
        # Run ffprobe to get video information in JSON format
        cmd = [
            'ffprobe',
            '-v', 'error',
            '-select_streams', 'v:0',
            '-show_entries', 'stream=width,height,duration,codec_name,bit_rate',
            '-of', 'json',
            filename
        ]
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)

        # Parse the JSON output
        video_info = json.loads(result)

        # Extract relevant data
        width = video_info['streams'][0]['width']
        height = video_info['streams'][0]['height']
        duration = video_info['streams'][0]['duration']
        codec_name = video_info['streams'][0]['codec_name']
        bit_rate = video_info['streams'][0]['bit_rate']

        # Print the relevant data
        print(f"Video Width: {width} pixels")
        print(f"Video Height: {height} pixels")
        print(f"Video Duration: {duration} seconds")
        print(f"Video Codec: {codec_name}")
        print(f"Video Bitrate: {bit_rate} bps")

    except subprocess.CalledProcessError as e:
        print(f"Error running ffprobe: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# ---- 1 ----
# convert_to_mp2("BBB.mp4")

# ---- 2 ----
#resize_input("BBB.mp4")

# ---- 3 ----
#change_chroma_sub("BBB.mp4")

# ---- 4 ----
#get_video_info("BBB.mp4")


# ---- 5 ----
#Inheritance from a file in a different folder from P1
import sys
import os

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Calculate the path to the directory containing rgb_yuv.py
P1_folder_dir = os.path.join(current_dir, '../P1_PauSegalésTorres')

# Add the yuv_rgb_dir to the Python path
sys.path.append(P1_folder_dir)


# Now you can import functions from yuv_rgb.py
from DCT import DCTConverter 
import numpy as np

dct_converter = DCTConverter()

# Create a sample input matrix (you can use your own data)
input_matrix = np.array([[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12],
                         [13, 14, 15, 16]])

# Perform forward DCT
dct_transformed_matrix = dct_converter.forward_dct(input_matrix)
print("DCT-transformed matrix:")
print(dct_transformed_matrix)

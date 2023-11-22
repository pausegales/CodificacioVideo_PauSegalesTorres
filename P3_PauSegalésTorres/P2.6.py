import os

# Replace these paths with your input video and output video paths
input_video = 'BBB.mp4'
output_video = 'output_video_with_histogram.mp4'

# Create a temporary directory to store intermediate files
temp_dir = 'temp'
os.makedirs(temp_dir, exist_ok=True)

# Generate full paths for files
histogram_file = os.path.join(temp_dir, 'histogram.yuv')

# Step 1: Extract the YUV histogram from the input video
extract_histogram_command = f"ffmpeg -i {input_video} -filter_complex \
                            \"split=2[original][histogram]; \
                            [histogram]waveform=m=0:s=hd720:color=full:filter=flat,format=yuv420p[v]\" \
                            -map [v] -f rawvideo {histogram_file}"
os.system(extract_histogram_command)

# Step 2: Create a video displaying the histogram
if os.path.exists(histogram_file):
    create_video_command = f"ffmpeg -i {input_video} -i {histogram_file} -filter_complex \
                            \"[0:v][1:v]overlay=W-w-10:H-h-10:format=auto,format=yuv420p\" \
                            {output_video}"
    os.system(create_video_command)
    
    # Optional: Clean up the extracted histogram file
    os.remove(histogram_file)
else:
    print("Histogram file not found. Extraction failed.")

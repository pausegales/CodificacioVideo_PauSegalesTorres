import os

# Replace these paths with your input video, subtitle, and output video paths
input_video = 'BigBuckBunny.mp4'
subtitle_file = 'Big_Buck_Bunny_English.srt'
output_video = 'output_video_with_subtitles.mp4'

# Command to burn subtitles onto the video
command = f"ffmpeg -i {input_video} -vf subtitles={subtitle_file} {output_video}"

# Execute the command using os.system
os.system(command)

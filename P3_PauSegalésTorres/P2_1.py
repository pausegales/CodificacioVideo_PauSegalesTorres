import os

def visualize_macroblocks_motion_vectors(input_video, output_video):
    # Command to generate a video showing macroblocks and motion vectors
    command = "ffmpeg -flags2 +export_mvs -i " + input_video + " -vf codecview=mv=pf+bf+bb " + output_video

    # Execute the ffmpeg command
    os.system(command)


# Replace 'input_video.mp4' with the path to your input video
input_video_path = 'BBB.mp4'

# Replace 'output_video_with_visualization.mp4' with the desired output video path
output_video_path = 'BBB_out.mp4'

# Call the method to create the video with visualizations
visualize_macroblocks_motion_vectors(input_video_path, output_video_path)

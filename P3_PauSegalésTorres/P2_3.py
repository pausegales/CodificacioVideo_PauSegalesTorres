import subprocess
import json

def count_tracks_in_container(input_file):
    ffprobe_cmd = f'ffprobe -v error -show_entries stream=codec_type -of json {input_file}'
    
    # Run ffprobe command to get stream information
    try:
        result = subprocess.run(ffprobe_cmd, capture_output=True, text=True, shell=True)
        stream_info = json.loads(result.stdout)
        
        # Count tracks of each type
        audio_tracks = sum(1 for stream in stream_info['streams'] if stream['codec_type'] == 'audio')
        video_tracks = sum(1 for stream in stream_info['streams'] if stream['codec_type'] == 'video')
        subtitle_tracks = sum(1 for stream in stream_info['streams'] if stream['codec_type'] == 'subtitle')

        print(f"Audio Tracks: {audio_tracks}")
        print(f"Video Tracks: {video_tracks}")
        print(f"Subtitle Tracks: {subtitle_tracks}")
        
        total_tracks = audio_tracks + video_tracks + subtitle_tracks
        print(f"Total Tracks: {total_tracks}")
        
        return total_tracks

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Provide the input MP4 file for analysis
input_file = 'output_bbb_container.mp4'  # Replace with the path to your MP4 file
count_tracks_in_container(input_file)

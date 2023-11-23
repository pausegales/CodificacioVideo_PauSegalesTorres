import subprocess
import os
import json

def merge_videos(input_file1, input_file2, output_file):
    # FFmpeg command to merge two videos side by side
    command = f'ffmpeg -i {input_file1} -i {input_file2} -filter_complex hstack=inputs=2 {output_file}'
    os.system(command)

def get_video_info(filename):
    # Execute ffprobe command to get video information in JSON format
    command = f'ffprobe -v quiet -print_format json -show_format -show_streams {filename}'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    
    # Load the JSON data
    try:
        video_info = json.loads(result.stdout)
        return video_info
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

def compare_video_info(video_info1, video_info2):
    if video_info1 is None or video_info2 is None:
        print("Error: Couldn't retrieve video information.")
        return

    print("Comparing Video Information:")
    print(f"{'Characteristic': <30}{'Video 1': <20}{'Video 2': <20}")
    print("=" * 70)

    characteristics = [
        'duration', 'bit_rate', 'codec_name', 'width', 'height', 'avg_frame_rate' ]

    for characteristic in characteristics:
        info1 = get_video_attribute(video_info1, characteristic)
        info2 = get_video_attribute(video_info2, characteristic)

        print(f"{characteristic: <30}{str(info1): <20}{str(info2): <20}")

def get_video_attribute(video_info, attribute):
    # Get the attribute from video information if present, otherwise return '-'
    if 'streams' in video_info:
        for stream in video_info['streams']:
            if attribute in stream:
                return stream[attribute]
    return '-'

def main():
    # Replace these with the paths to your video files
    video_file1 = 'output_360x240_AV1.mp4'
    video_file2 = 'output_360x240_H.265.mp4'
    output_file = 'video_compare.mp4'
    # Get information for both videos
    video_info1 = get_video_info(video_file1)
    video_info2 = get_video_info(video_file2)

    # Compare video information
    compare_video_info(video_info1, video_info2)

    merge_videos(video_file1, video_file2, output_file)

    print("\nAs you can see, regarding the data information there is no difference")
    print("between the two codecs. So the differences will be seen in the videos")
    print("side by side (check: video_compare.mp4). Where the effects of the compression will be seen")
    print("It seems that with very high frequency movements the AV1 codec behaves better, peixelating less")
    print("the surroundings of the things that seem to be occuded by whet is moving.")


    print(" ----------\-----\-----\-----\----------\n")

if __name__ == "__main__":
    main()

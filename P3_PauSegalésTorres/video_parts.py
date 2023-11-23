import os
import subprocess
import json

from P2_4 import subtitles

class CaseHandler:
    def __init__(self):
        pass
    
    def visualize_macroblocks_motion_vectors(input_video, output_video):
        # Command to generate a video showing macroblocks and motion vectors
        command = "ffmpeg -flags2 +export_mvs -i " + input_video + " -vf codecview=mv=pf+bf+bb " + output_video
        # Execute the ffmpeg command
        os.system(command)

    def create_bbb_container():
        input_file = 'BigBuckBunny.mp4'

        # Cut BBB into a 50-second video
        os.system(f'ffmpeg -i {input_file} -ss 0 -t 50 -c:v copy -c:a copy bbb_50s.mp4')

        # Export BBB(50s) audio as MP3 mono track
        os.system('ffmpeg -i bbb_50s.mp4 -ac 1 bbb_50s_mono.mp3')

        # Export BBB(50s) audio in MP3 stereo with lower bitrate
        os.system('ffmpeg -i bbb_50s.mp4 -ac 2 -b:a 64k bbb_50s_stereo_low_bitrate.mp3')

        # Export BBB(50s) audio in AAC codec
        os.system('ffmpeg -i bbb_50s.mp4 -strict experimental -ac 2 -b:a 128k -c:a aac bbb_50s_aac.aac')

        # Package everything in a .mp4 with FFMPEG
        os.system('ffmpeg -i bbb_50s.mp4 -i bbb_50s_mono.mp3 -i bbb_50s_stereo_low_bitrate.mp3 -i bbb_50s_aac.aac -c:v copy -c:a copy -map 0:v:0 -map 1:a:0 -map 2:a:0 -map 3:a:0 output_bbb_container.mp4')

   
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

    
    
    def handle_case(self, choice):
        if choice == 1:
            print("Performing 1st exercise")
            self.visualize_macroblocks_motion_vectors('BBB.mp4', 'BBB_out.mp4')


        elif choice == 2:
            print("Performing Case 2nd exercise")
             # Call the function to create the BBB container with the specified requirements
            self.create_bbb_container()
            

        elif choice == 3:
            print("Performing Case 3rd exercise")
            self.count_tracks_in_container("output_bbb_container.mp4")


        elif choice == 4:
            print("The 4th exercise is to create a different script")
            print("Call exercise 5 to inherit and call its function from here")


        elif choice == 5:
            print("Performing Case 5th exercise")
            subtitles()

    def run(self):
        print("Choose an option:")
        print("1. Case 1")
        print("2. Case 2")
        print("3. Case 3")
        print("4. Case 4")
        print("5. Case 5")

        while True:
            try:
                choice = int(input("Enter your choice (1-5): "))
                if choice < 1 or choice > 5:
                    print("Please enter a number between 1 and 5.")
                else:
                    self.handle_case(choice)
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    handler = CaseHandler()
    handler.run()

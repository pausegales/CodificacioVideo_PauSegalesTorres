import os

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

# Call the function to create the BBB container with the specified requirements
create_bbb_container()

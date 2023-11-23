import os

def convert_video(input_file, output_file, resolution, codec=None):
    if codec:
        command = f'ffmpeg -i {input_file} -vf scale={resolution} -c:v {codec} -c:a copy {output_file}'
    else:
        command = f'ffmpeg -i {input_file} -vf scale={resolution} {output_file}'
    os.system(command)

def main():
    input_video = 'BBB.mp4'

    resolutions = {
        #'720p': '1280x720',
        ##'480p': '854x480',
        '360x240': '360x240',
        '160x120': '160x120'
    }

    codecs = {
        'VP8': 'libvpx',
        'VP9': 'libvpx-vp9',
        'H.265': 'libx265',
        'AV1': 'libaom-av1'
    }

    # Convert to different resolutions
    for resolution_name, resolution_value in resolutions.items():
        output_file = f'output_{resolution_name}.mp4'
        convert_video(input_video, output_file, resolution_value)
        print(f'Conversion to {resolution_name} completed. Output: {output_file}')

    # Convert different resolutions to various codecs
    for resolution_name in resolutions.keys():
        input_file = f'output_{resolution_name}.mp4'
        for codec_name, codec_value in codecs.items():
            if 'VP' in codec_name:
                output_file = f'{os.path.splitext(input_file)[0]}_{codec_name}.webm'
            else:
                output_file = f'{os.path.splitext(input_file)[0]}_{codec_name}.mp4'
            convert_video(input_file, output_file, resolutions[resolution_name], codec_value)
            print(f'Conversion of {resolution_name} to {codec_name} completed. Output: {output_file}')

if __name__ == "__main__":
    main()

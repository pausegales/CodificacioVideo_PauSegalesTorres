import os

def bw_ffmpeg(filename):

    #The output file has a bigger size than the original image eventhough it is a monochrome image.
    os.system('ffmpeg -i ' + filename + ' -vf format=gray,maskfun=low=128:high=128:fill=0:sum=128 image-bw.jpeg')

    #os.system('ffmpeg -i ' + filename + ' -vf hue=s=0 bw.jpeg')
    #os.system('ffmpeg -i ' + filename + ' -filter_complex "extractplanes=y" y.jpg')
    #os.system('ffmpeg -f concat -i ' + filename + ' -vf format=gray,maskfun=low=128:high=128:fill=0:sum=128 output_gray.png')
    #os.system('ffmpeg -i ' + filename + ' -vf "format=gray,format=yuv420p" -q:v 2 -c:v mjpeg bw.jpeg')

# ---- 4 ----
bw_ffmpeg("baixa.jpeg")
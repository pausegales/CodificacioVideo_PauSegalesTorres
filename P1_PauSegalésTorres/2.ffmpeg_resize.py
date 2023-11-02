import os

def resize_ffmpeg(filename):
    #Calling the system terminal with an ffmpeg command
    os.system('ffmpeg -i ' + filename + ' -vf scale="100:-1" output.jpeg')


# ---- 2 ----
resize_ffmpeg("baixa.jpeg")
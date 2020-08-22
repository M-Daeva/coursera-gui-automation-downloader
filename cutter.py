from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
import os


def cut_video(src, dist, start, end):
    video = VideoFileClip(src)
    end = video.end - end
    ffmpeg_extract_subclip(src, start, end, targetname=dist)
    video.reader.close()
    video.audio.reader.close_proc()


def cut_all(path, start, end):
    names = os.listdir(path)
    os.mkdir(path + '\\' + 'dist')
    for name in names:
        cut_video(path + '\\' + name, path + '\\dist\\' + name, start, end)

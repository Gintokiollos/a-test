from __future__ import unicode_literals
import youtube_dl ,glob
from moviepy.editor import *
path='E:\a-test'
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/playlist?list=PLiFNg5fXiX32p4RMMDCUpjVEwXOnqyTj_'])
videoclip = VideoFileClip(path)
audioclip = videoclip.audio
audioclip.write_audiofile(path)
audioclip.close()
videoclip.close()
for infile in glob.glob(os.path.join(path,'*.mp4')): #找出垃圾並刪除
    os.remove(infile)
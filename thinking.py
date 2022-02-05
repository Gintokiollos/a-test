import sys
from moviepy.editor import *
import you_get
import os
import glob
def download(url, path):
    sys.argv = ['you-get','-o', path ,'-l', url]
    you_get.main()
if __name__ == '__main__':
     # 视频网站的地址
    url = input("你需要下載的內容:")
    # 视频输出的位置
    path = input("下載位置:")
    download(url, path)
videoclip = VideoFileClip(path) #
audioclip = videoclip.audio
audioclip.write_audiofile(path)
audioclip.close()
videoclip.close()
for infile in glob.glob(os.path.join(path,'*.srt')): #找出垃圾並刪除
    os.remove(infile)
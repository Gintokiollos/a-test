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
videoclip = VideoFileClip(path)
audioclip = videoclip.audio
audioclip.write_audiofile(path)
audioclip.close()
videoclip.close()
srt_files = glob.glob('test_dir/*.srt')

for py_file in srt_files:
    try:
        os.remove(py_file)
    except OSError as e:
        print(f"Error:{ e.strerror}")
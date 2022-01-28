
from urllib import request
import re,requests
betrayal = []
url = 'http://renxueyanjiu.com/index.php?m=content&c=index&a=show&catid=122&id=2951'
html = requests.get(url)
html.text
html.content
html.status_code
if html.status_code ==200:
    info1=(html.text)
    pattern1=re.compile(r'(?<=、)\w+')
    idiom=pattern1.findall(info1)
    gu=len(idiom)
    for i in range(gu):
        if  len(idiom[i]) == 4 and idiom[i] != '人学研究' :
            betrayal.append(idiom[i])
    #print(betrayal)
    pattern2=re.compile(r'(?<=【释义】)\w+')
    Paraphrase=pattern2.findall(info1)
    print(Paraphrase)
else:
    print('連線不成功')
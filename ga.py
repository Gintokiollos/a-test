
from urllib import request
import re,requests
betrayal = []
url = 'http://renxueyanjiu.com/index.php?m=content&c=index&a=show&catid=122&id=2951'
html = requests.get(url)
html.text
html.content
html.status_code
if html.status_code ==200:
    info3=(html.text)
    pattern3=re.compile(r'(?<=、)\w+')
    idiom=pattern3.findall(info3)
    gu=len(idiom)
    for i in range(gu):
        if  len(idiom[i]) == 4 and idiom[i] != '人学研究' :
            betrayal.append(idiom[i])
    print(betrayal)

else:
    print('連線不成功')

from urllib import request
import re,requests
a = []
url = 'http://renxueyanjiu.com/index.php?m=content&c=index&a=show&catid=122&id=2951'
html = requests.get(url)
html.text
html.content
html.status_code
if html.status_code ==200:
    info3=(html.text)
    pattern3=re.compile(r'(?<=、)\w+')
    f3=pattern3.findall(info3)
    gu=len(f3)
    for i in range(gu):
        if  len(f3[i]) != 4 or f3[i] == '人学研究' :
            a.append(i)
    print(a)
    print(f3,sep="\n")
else:
    print('連線不成功')
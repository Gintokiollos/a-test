
from urllib import request
import re,requests

url = 'http://renxueyanjiu.com/index.php?m=content&c=index&a=show&catid=122&id=2951'
html = requests.get(url)
html.text
html.content
html.status_code
if html.status_code ==200:
    info3=(html.text)
    pattern3=re.compile(r'(?<=、)\w+')
    f3=pattern3.findall(info3)
    print(f3,sep="\n")
else:
    print('連線不成功')
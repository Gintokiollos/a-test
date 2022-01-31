
from urllib import request
import re,requests,json
betrayal = []
url = 'http://renxueyanjiu.com/index.php?m=content&c=index&a=show&catid=122&id=2951'
html = requests.get(url) #讀取網址
html.text #讀取文字
html.content #讀取內容
html.status_code #讀取讀取
def hhh(betrayal, html):
    info1=(html.text)
    pattern1=re.compile(r'(?<=、)\w+') #設定判定式以抽取關鍵字後的文字
    idiom=pattern1.findall(info1) 
    for i in range(len(idiom)):
        if  len(idiom[i]) == 4 and idiom[i] != '人学研究' : #垃圾分類
            betrayal.append(idiom[i])
    print(betrayal)

if html.status_code ==200: #判斷讀取是否成功
    hhh(betrayal, html)
    a=[]
    for i in range(len(betrayal)): #整一堆數字出來
        a.append(i)
    json1=[dict(zip(a,betrayal))] #幫成語打學號
    json2=json.dumps(json1,indent=2,ensure_ascii=False)#壓成json格式
    print(json2)
    with open('E:\data.json', "w") as f:   #打開檔案
        f.write(json2)  #寫入檔案
        f.close()       #停止寫入
    #pattern2=re.compile(r'(?<=【释义】)\w+\S\w+\S') #咕咕咕
    #Paraphrase=pattern2.findall(info1)
    #print(Paraphrase)
else:
    print('連線不成功')
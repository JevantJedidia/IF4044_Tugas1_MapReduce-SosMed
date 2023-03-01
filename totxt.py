import os
import json

fbFile = open("txt/fb.txt","w")
igFile = open("txt/ig.txt","w")
twtFile = open("txt/twt.txt","w")
ytFile = open("txt/yt.txt","w")
otherFile = open("txt/other.txt","w")

for filename in os.listdir('./rawjson/raw_json'):
    # print(filename)
    filename = "rawjson/raw_json/" + filename
    print(filename)
    # print(filename)
    if ("youtube" in filename):
        f = open(filename,'r',encoding="utf8")
        data = json.load(f)
        ytFile.write(json.dumps(data))
        ytFile.write('\n')
    elif ("twitter" in filename):
        f = open(filename,'r',encoding="utf8")
        data = json.load(f)
        twtFile.write(json.dumps(data))
        twtFile.write('\n')
    elif ("facebook" in filename):
        f = open(filename,'r',encoding="utf8")
        data = json.load(f)
        fbFile.write(json.dumps(data))
        fbFile.write('\n')
    elif ("instagram" in filename):
        f = open(filename,'r',encoding="utf8")
        data = json.load(f)
        igFile.write(json.dumps(data))
        igFile.write('\n')
    else:
        f = open(filename,'r',encoding="utf8")
        data = json.load(f)
        otherFile.write(json.dumps(data))
        otherFile.write('\n')

ytFile.close()
fbFile.close()
twtFile.close()
igFile.close()
otherFile.close()
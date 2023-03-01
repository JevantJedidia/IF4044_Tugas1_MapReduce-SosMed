#!/home/bigdata/anaconda3/bin/python
import json
import sys
import datetime
import time as t

def parseTime(type, time):
    if type == "facebook":
        return time[:10]
    elif type == "instagram":
        return str(time.date())
    elif type == "twitter":
        return time[:10]
    elif type == "youtube":
        return time[:10]
    else:
        return time[:10]

def addCount(date, dict):
    if date in dict:
        dict[date] += 1
    else:
        dict[date] = 1

# for line in sys.stdin:
#     file.append(json.loads(line))
other = ['anaktester_go', 'byu.id', 'gridoto', 'myxl', 'telkomsel']

for line in sys.stdin:
    isi = line.strip()
    f = json.loads(isi)

    for data in f:
        # print(json.dumps(data, indent=4, sort_keys=True))
        if (data == "GraphImages"):
            for item in f[data]:
                if 'taken_at_timestamp' in item:
                    # print(json.dumps(item['taken_at_timestamp'], indent=4, sort_keys=True))
                    socMedType = other[0]
                    time = datetime.datetime.fromtimestamp(int(item["taken_at_timestamp"]))
                    date = parseTime(socMedType, str(time))
                    print(socMedType, "\t", date, "\t", 1)
                if 'comments' in item:
                    for komen in item['comments']['data']:
                        socMedType = other[0]
                        time = datetime.datetime.fromtimestamp(int(komen["created_at"]))
                        date = parseTime(socMedType, str(time))
                        print(socMedType, "\t", date, "\t", 1)
            other.pop(0)
                    
        else:
            if "crawler_target" in data:
                socMedType = data["crawler_target"]["specific_resource_type"]
            else:
                socMedType = data["object"]["social_media"]
            #Map Faceboook
            if socMedType == "facebook":
                time = data["created_time"]
                date = parseTime(socMedType, time)
                print(socMedType, "\t", date, "\t", 1)
                # addCount(date, dict)
                comment = data["comments"]["data"]
                for komen in comment:
                    time = komen["created_time"]
                    date = parseTime(socMedType, time)
                    print(socMedType, "\t", date, "\t", 1)
                    # addCount(date, dict)
            #Map Instagram
            elif socMedType == "instagram":
                time = datetime.datetime.fromtimestamp(int(data["created_time"]))
                date = parseTime(socMedType, time)
                print(socMedType, "\t", date, "\t", 1)
                # addCount(date, dict)
            elif socMedType == "twitter":
                time = data['created_at']
                ts = t.strftime('%Y-%m-%d %H:%M:%S', t.strptime(time,'%a %b %d %H:%M:%S +0000 %Y'))
                date = parseTime(socMedType, ts)
                print(socMedType, "\t", date, "\t", 1)
                # addCount(date, dict)
            elif socMedType == "youtube":
                if "topLevelComment" in data['snippet']:
                    time = data['snippet']['topLevelComment']['snippet']['publishedAt']
                    date = parseTime(socMedType, time)
                    print(socMedType, "\t", date, "\t", 1)
                        # addCount(date, dict)
                else:
                    time = data['snippet']['publishedAt']
                    date = parseTime(socMedType, time)
                    print(socMedType, "\t", date, "\t", 1)
                    # addCount(date, dict)

# test = 0
# for key in dict:
#     print(socMedType, "\t", key, "\t", dict[key])
#     test += dict[key]
# print(test)


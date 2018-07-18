import json
with open("music_show.txt","w+", encoding='utf-8-sig') as g:
    with open("music_show.json","r", encoding='utf-8-sig') as f:
        s=json.load(f)
        for i in range(len(s)):
            g.write(s[i]["title"]+":"+s[i]["startDate"]+"~"+s[i]["endDate"]+"\n")
    
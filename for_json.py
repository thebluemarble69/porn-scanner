import json
import time

def f(s):
    if len(s) > 0:
        return s[len(s) - 1].get("id")
    else:
        return 0

def rite(a):
    with open('for_python.json', 'r', encoding="utf-8") as sex:
        dum = json.load(sex)
        if dum == "null":
            dum = []
    temp = f(dum)
    obj = {"id": temp + 1, str(int(time.time())): a}
    dum.append(obj)
    with open('for_python.json', 'w', encoding="utf-8") as sexy:
        json.dump(dum, sexy, ensure_ascii=False, indent=4)

def red():
    with open('for_python.json', 'r', encoding="utf-8") as d:
        print(d.read())

def delete(s):
    with open("for_python.json", "r", encoding="utf-8") as da:
        data = json.load(da)
    if s <= len(data):
        data = [i for i in data if i['id'] != s]
        for i, ob in enumerate(data):
            ob['id'] = i+1
        with open("for_python.json", "w", encoding="utf-8") as fd:
            json.dump(data, fd, ensure_ascii=False, indent=4)
        print('deleted')
    else:
        print('invalid id number.')

while True:
    d = input('jive ').strip()
    if d.lower() == "read":
        red()
    elif d.startswith("delete "):
        try:
            g = d.split(" ")[1]
            delete(int(g))
            #print("deleted")
        except:
            print("usage: delete <id>(int)")
            continue
    elif d.lower() == "exit":
        quit()
    elif d == "Clear":
        with open("for_python.json", "w", encoding="utf-8") as e:
            e.write("[]")
    
    elif d != "":
        rite(d)
        print('done')
    else:
        continue

        
        
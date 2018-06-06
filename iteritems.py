dic = {"a":1}
dic.get("a")
dic = {"a":[1]}
for item in dic.iteritems():
    print item
%hist -f iteritems.py
for _ , item in dic.iteritems():
    print item
%hist -f iteritems.py
dic = {"a":[1], "b":[2], "c":[3], "d":[4]}
for _ , item in dic.iteritems():
    print item
%hist -f iteritems.py

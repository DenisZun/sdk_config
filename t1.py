# -*- coding:utf-8-*-
import sys
import json
import urllib
import base64

meta_option= json.dumps({"s":"WAP","n":"京东官网","id":"`https://m.jd.com`"})
data = meta_option.decode("utf-8").encode('gb2312')
# data = urllib.quote(base64.b64encode(data))  # eyJzIjogIldBUCIsICJpZCI6ICJgaHR0cHM6Ly9tLmpkLmNvbWAiLCAibiI6ICJcdTRlYWNcdTRlMWNcdTViOThcdTdmNTEifQ%3D%3D
data = urllib.quote_plus(base64.b64encode(data))
print data





# data = json_data.decode("utf-8").encode('gb2312')
#
#
# # print type(data)
# data = base64.b64encode(data)
#
# url_data = urllib.quote_plus(data)  # eyJzIjogIldBUCIsICJpZCI6ICJgaHR0cHM6Ly9tLmpkLmNvbWAiLCAibiI6ICJcdTRlYWNcdTRlMWNcdTViOThcdTdmNTEifQ%3D%3D
#
# # url_data = urllib.urlencode(data) # 只能为字典

# eyJzIjogIldBUCIsICJpZCI6ICJgaHR0cHM6Ly9tLmpkLmNvbWAiLCAibiI6ICJcdTRlYWNcdTRlMWNcdTViOThcdTdmNTEifQ==
# eyJzIjoiV0FQIiwibiI6Ir6ptqu52c34IiwiaWQiOiJodHRwczovL20uamQuY29tIn0%3d
# url_data = urllib.quote_plus(str(data))

# print url_data

# a = u"京东官网"
# # b = a.decode("utf-8").encode("gb2312")
# b = a.encode("gb2312")
#
# print type(b)
# print b
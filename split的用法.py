str = "00000003210Runoob01230000000"
print str.strip( '0' )
str2 = "   Runoob      "
print str2.strip(" ")
str = "123abcrunoob321"
print str.strip("123")
str = "0000000this is string 0000example....wow!!!0000000"
print str.strip("0")
# 中间部分是不会被移除的
str1 = '    iam string  '
print "str1:\'%s\'" %str1
print "str1.strip(" "):\'%s\'" %str1
print "str1.strip(" "):\'%s\'" %str1.strip(" ")
print "str1.strip():\'%s\'" %str1.strip()
str2 = '@@@@@iamstring@@@@@'
print "str2.strip('@'):\'%s\'" %str2.strip('@')
print "str2.strip('@@'):\'%s\'" %str2.strip('@@')
import requests
requests.get("http://www.baidu.com").text
%hist -f split的用法.py

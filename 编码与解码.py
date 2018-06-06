a = "支付宝"
a
b = a.decode("gbk")
b = a.decode("utf-8")
b
type(b)
b = a.decode("utf-8").encode("gb2312")
b
type(b)
%hist -f 编码与解码.py

#-*- coding:utf-8 -*-
import hashlib



"""
http://pay.payshelp.com/?uid=49
&qr_amount=10
&notify_url=http://payment.zcjbdw.com/8001/304/pay_notice
&return_url=www.baidu.com
&order_number=345867345
&order_uid=67545
&type=2
&key=8D415DD5E246CCD0607EC8850D171662

"""

params = {}
params['uid'] = '49'  # 商户号
params['qr_amount'] = 128  # 下单金额
params['notify_url'] = 'http://payment.zcjbdw.com/8001/304/pay_notice'  # 支付回调地址
params['return_url'] = 'www.TGBUS.com'  # 跳转地址
params['order_number'] = '23112312312'  # 商户订单号
params['order_uid'] = 'denis'  # 客户号
params['type'] = 2  # 支付渠道

def make_key(params):
    keys = ('notify_url', 'order_number','order_uid', 'qr_amount', 'return_url', 'type', 'uid')
    sign_str = ''.join([str(params.get(key, "")) for key in keys])
    sign_str += ''
    print sign_str
    sign = hashlib.md5(sign_str).hexdigest().upper()
    print "sign:%s" % sign
    return sign


if __name__ == '__main__':
    params['key'] = make_key(params)  # 秘钥
    print params
    make_key(params)


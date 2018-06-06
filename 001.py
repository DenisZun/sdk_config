def is_order_success(params):
    if params == 1:
        return True
    return False


def check_order(params):
    if is_order_success(params):
        print "======"


def check_sign(params):
    if params == 1:
        print is_order_success(params)
    else:
        print is_order_success(params)
    return is_order_success(params)

if __name__ == '__main__':
    check_sign(1)

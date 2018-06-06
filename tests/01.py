plat_id = 269

log_base_name = ""


def foo(func):
    def wrapper():
        if plat_id == 301:
            global platform_info
            global log_base_name
            platform_info = dict(nPlatformID="ePlatform_myjfzfb", szPrefix="myjfzfb_")
            log_base_name = "myjfzfb"
        elif plat_id == 269:
            platform_info = dict(nPlatformID="ePlatform_zfbpc1", szPrefix="zfbpc1")
            log_base_name = "zfbpc1"
        return func()
    return wrapper

@foo
def get_plaform_info():
    return platform_info


print get_plaform_info()
print log_base_name

# platform_info = dict(nPlatformID=ePlatform_myjfzfb, szPrefix="myjfzfb_")
# log_base_name = "myjfzfb"

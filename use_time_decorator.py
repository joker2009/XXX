# 装饰器，用来计算函数运行时间
def print_run_time(func):
    def wrapper(*args, **kw):
        start_time = time.time()
        res = func(*args, **kw)
        end_time = time.time()
        use_time = end_time - start_time
        # # 以下时间转换
        # s = int(use_time)
        # h = s / 3600
        # m = (s - h * 3600) / 60
        # ss = s - h * 3600 - m * 60
        # format_use_time = str(h) + "小时" + str(m) + "分钟" + str(ss) + "秒"
        log.logger.debug("{} 用时 {}".format(func.__name__, use_time))
        return res
    return wrapper

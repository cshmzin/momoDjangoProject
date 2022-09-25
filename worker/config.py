import time

def timer(fcn):
    def inner(*args, **kwargs):
        start_time = time.time()
        fcn(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return inner

@timer
def Test():
    time.sleep(1)

test = Test()

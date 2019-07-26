import time
i = 0
hoge = 0
while i<60:
    time.sleep(1)
    hoge += 360/60
    print(hoge)
    i += 1
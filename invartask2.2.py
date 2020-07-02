import random
import time

def uuid():
    raw_header = 'BRUH'
    header = ''.join(hex(ord(ch))[2:].zfill(2) for ch in raw_header)

    now = time.localtime()
    hour = hex(int(str(now.tm_hour).zfill(2)))[2:]
    minute = hex(int(str(now.tm_min).zfill(2)))[2:]
    salt1 = ''.join((hour, minute))

    salt2 = ''.join(hex(random.randint(0, 255))[2:].zfill(2) for i in range(2))

    data = ''.join(hex(random.randint(0, 255))[2:].zfill(2) for i in range(4))

    yield '-'.join((header, salt1, salt2, data))


uuid_gen = uuid()
for item in uuid_gen:
    print(item)


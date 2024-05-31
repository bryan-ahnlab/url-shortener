import string
import uuid

BASE62 = string.digits + string.ascii_letters

def encode_base62(uuid_val):
    num = int(uuid_val, 16)
    if num == 0:
        return BASE62[0]
    arr = []
    base = len(BASE62)
    while num:
        num, rem = divmod(num, base)
        arr.append(BASE62[rem])
    arr.reverse()
    return ''.join(arr)

def shorten_uuid():
    new_uuid = uuid.uuid4()
    base62_encoded = encode_base62(new_uuid.hex)
    return base62_encoded[:7]
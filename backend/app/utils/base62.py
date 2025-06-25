import string
import uuid

BASE62 = string.digits + string.ascii_letters


def encode_base62(raw_uuid):
    num = int(
        raw_uuid, 16
    )  # Convert the raw UUID to an integer (16 진수 문자열을 10 진수 정수로 변환)
    if num == 0:
        return encode_base62(uuid.uuid4().hex)
    arr = []  # Initialize an empty list to store the base62 encoded characters
    base = len(BASE62)  # Get the length of the base62 alphabet (62)
    while num:
        num, rem = divmod(
            num, base
        )  # Divide the number by the base and get the remainder
        arr.append(BASE62[rem])
    arr.reverse()
    return "".join(arr)


def shorten_uuid():
    raw_uuid = uuid.uuid4()  # Generate a random UUID using uuid4()
    base62_encoded_uuid = encode_base62(
        raw_uuid.hex
    )  # Encode the UUID to base62 (UUID를 32자리 16진수 문자열로 변환하여 다시 인코딩)
    return base62_encoded_uuid[
        :7
    ]  # Return the first 7 characters of the base62 encoded UUID

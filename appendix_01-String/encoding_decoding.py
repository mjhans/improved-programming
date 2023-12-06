str = "안녕"

enc = str.encode("utf-8")
print(enc)

dec = enc.decode("utf-8")
print(dec)

dec2 = enc.decode("utf-16")
print(dec2)

dec3 = enc.decode("utf-16-le")
print(dec3)

dec4 = enc.decode("utf-16-be")
print(dec4)


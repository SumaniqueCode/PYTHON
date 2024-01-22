import random, math

def genarateOTP():
    OTP = ""
    for i in range(1,6):
        # a = random.random()
        # b = math.floor(a*10) 

        b = random.randint(0,9)
        OTP += str(b)
    return OTP

print(genarateOTP())
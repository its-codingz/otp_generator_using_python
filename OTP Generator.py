import random as r

def otpgen():
    otp = ""
    for i in range(4):
        otp += str(r.randint(1,9))
    print("Your OTP is:",otp)

otpgen()

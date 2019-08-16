class Study_3():

    def __init__(self,a):
        self.a = a

    def sout_time(self):
        payback1 = 1024 - self.a
        num1 = int(payback1 / 64)
        payback2 = payback1 - num1 * 64
        num2 = int(payback2 / 16)
        payback3 = payback2 - num2 * 16
        num3 = int(payback3 / 4)
        num4 = payback3 % 4
        print(num1 + num2 + num3 + num4)

a = int(input())
study = Study_3(a)
study.sout_time()

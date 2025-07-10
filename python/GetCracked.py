class SmallNumbers:
    def run(self):
        a = 1
        b = 1
        if (a is b):
            print("A")
        else:
            print("B")

        a = 257
        b = 257
        if (a is b):
            print("C")
        else:
            print("D")

        a = int("-6")
        b = -6
        if (a is b):
            print("E")
        else:
            print("F")

class InPlaceAssignment:
    def run(self):
        t = (1, 2, [30, 40])
        t[2] += [50, 60]

class SimpleType:
    def run(self):
        a=(1)
        print(type(a))

class DefaultArguments:
    def run(self):
        print(self.myAppend(7), end =" ")
        print(self.myAppend(9))

    def myAppend(element, arr = []):
        arr.append(element)
        return arr

class DisMe:
    import dis
    def myFunction(self, x):
        y = x + 1
        return y * x

    def run(self):
        DisMe.dis.dis(self.myFunction)
        print(self.myFunction(5))
"""
class SimpleMath:
    from math import fma

    def run(self):
        print(int(self.fma(2, 2, 1_10_0)))
"""
class ZipIt:
    def run(self):
        arr1 = [1,2]
        arr2 = [1,2,3,4]
        arr3 = list(zip(arr1,arr2))
        print(len(arr3))
"""
class WhatAreWeReplacing:
    from copy import replace
    from collections import namedtuple

    def run(self):
		MyTuple = WhatAreWeReplacing.namedtuple("myTuple", ["x", "y"])
        t1 = MyTuple(1,2)
        t2 = WhatAreWeReplacing.replace(t1, x = 3)
        print(t1, t2)
"""

class MinMinister:
    def run(self):
        print(min(-0.0, False, round(7/2) - 4.0, float("nan"), key = lambda x: -x))
 
class ANumberWalksIntoABase:
    def run(self):
        print(0b10 + 0o10 + 0x10)

class A():
    __num=5
    def getNum(self):
        return self.__num

class MyNameIs():
    def run(self):
        a = A()
        a.__num=4

        print(f"{a.getNum()}{len(a.__dict__)}{a.__num}")

class SoHowBigIsX():
    import sys
    def run(self):
        x = 5
        print(self.sys.getsizeof(x))

class arrrg():
    def run(self):
        try:
            print(self.foo(1,2,3))
        except:
            print("option 1 fail")
        try:
            print(self.foo(1,b=2,c=3))
        except:
            print("option 2 fail")
        try:
            print(self.foo(a=1,b=1,c=1))
        except:
            print("option 3 fail")

    def foo(self,a, /, b, *, c):
        sum_val = a + b + c
        product_val = a * b * c
        return product_val // sum_val

class MaximalSnake():
    def run(self):
        x=1
        y=1
        print(x-----y)
if __name__ == "__main__":
    MaximalSnake().run()

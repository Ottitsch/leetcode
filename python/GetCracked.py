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
        a = (1)
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

class SimpleMath:
    from math import fma

    def run(self):
        print(int(self.fma(2, 2, 1_10_0)))

if __name__ == "__main__":
    SimpleMath().run()

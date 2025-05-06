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
    a = (1)
    print(type(a))

if __name__ == "__main__":
    SmallNumbers().run()

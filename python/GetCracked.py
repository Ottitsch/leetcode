class SmallNumbers:
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
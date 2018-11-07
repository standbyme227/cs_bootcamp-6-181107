a = 1


def outer():
    global a
    b = 2
    c = 3
    print("------------------------------------")
    print("global 선언으로 a를 바꾸기 전")
    print(a, b, c)
    print("------------------------------------")


    a = 100
    print("global 선언으로 a를 100으로 바꾼 후")
    print(a, b, c)
    print("------------------------------------")

    def inner():
        global a
        nonlocal b
        a = 1
        d = 4
        e = 5
        print("global 선언으로 a를 1로 바꾼 후")
        print(a, b, c, d, e)
        print("------------------------------------")


        b = 200
        d = 400

        a = 1000
        print("global 선언으로 a를 1000으로 nonlocal로 b는 200, d는 400으로 바꾼 후")
        print(a, b, c, d, e)
        print("------------------------------------")

    inner()


if __name__ == "__main__":
    outer()

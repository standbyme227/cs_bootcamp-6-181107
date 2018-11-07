# 변수를 선언한다.
g_var = 10

# 함수안에서 선언한 변수를 사용해서 프린트해본다.
def func():
    print("g_var = {}".format(g_var))

# 직접실행할때만 아래 함수를 실행한다.
if __name__ == "__main__":
    func()


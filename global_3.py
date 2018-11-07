# 전역변수를 선언한다
g_var = 10

# 힘수 내부에서 전역변수를 불러와 값을 바꾼다
def func():
    # global을 사용하면 전역변수를 가져다 올수 있다. (reference참조)
    global g_var
    # g_var에 새로운 갑을 대입한다.
    g_var = 20

# 직접실행
if __name__ == "__main__":
    # 프린트해서 처음 전역변수가 실행될때 값을 본다.
    print("g_var : {} before".format(g_var))
    # 함수를 실행한다.
    func()
    # 새로운 값이 적용되었는지 확인한다.
    print("g_var : {} after".format(g_var))

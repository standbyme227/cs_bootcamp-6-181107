# 변수를 선언한다.(전역변수)
g_var = 10

# 함수 내부에서 전역변수를 바꾸도록 실행한다.
def func():
    # 변수를 선언하는데 전역변수와 값은 이름으로 선언한다.(지역변수 선언)
    g_var=20
    # 프린트로 확인한다.
    print("g_var = {} in function".format(g_var))


# 직접실행했을때...
if __name__ == "__main__":
    # 함수를 실행해보고
    func()
    # 변수를 호출해본다.
    print("g_var = {} in main".format(g_var))


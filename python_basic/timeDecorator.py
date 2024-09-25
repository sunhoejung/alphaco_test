#Context Manager, Decorator
#클로저 : 함수 안에 또 다른 함수 생성

import time
#성능 확인용, 어디 함수든 위에 @써서 붙이면 실행 시간 출력됨
def time_decorator(func):       #코드 돌아가는 시간 체크하는 함수 // func : @time_decorator 아래 함수 의미
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@time_decorator      #사용자 정의 함수 위에 @써서 time_decorator 함수 호출 // 한번 함수 만들고 다른 함수 위에 @time_decorator쓰면 계속 쓸 수 있음
def slow_function():
    time.sleep(2)
    return "Finished"

# 사용 예시
slow_function()
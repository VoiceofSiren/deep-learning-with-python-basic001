class Light:
    def __enter__(self):
        print("불을 켭니다.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("불을 끕니다.")

'''
with
    - 컨텍스트 관리자(context manager)를 활용해 리소스를 안전하게 관리하기 위한 구문
    - 자원을 사용할 때 open → 작업 → close 과정을 깔끔하게 관리
    - 컨텍스트 매니저 객체의 __enter__ 와 __exit__ 메서드를 호출하는 문법
'''
with Light():
    print("방에서 책을 읽습니다.")

print("with 블럭 밖으로 나왔습니다.")
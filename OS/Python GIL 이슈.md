# Python GIL 이슈

## GIL? (Global Interpreter Lock)   
파이썬에서 멀티쓰레드 환경을 사용할 때 마주하게 되는 이슈.
하나의 스레드만 가지고 Python의 인터프리터를 제어할 수 있도록 하는 Mutex

특정 시점에서 오직 하나의 스레드만 실행 상태에 있을 수 있음을 의미함.
단일 스레드만 사용해서 프로그램을 실행하면 이러한 인슈가 없지만 Thread 모듈을 이용한 다중 스레드 코드에서 발생가능

```python
# 규문이 race condition 실습 ㅜㅜ
import threading

x=0
def plus():
    global x
    for i in range(100000000):
        x += 1
        
def minus():
    global x
    for i in range(100000000):
        x -= 1
        
t1 = threading.Thread(target=plus)
t2 = threading.Thread(target=minus)

t1.start()
t2.start()
t1.join()
t2.join()

print(x)
```
상기의 코드에서 plus와 minus 함수를 통해 계산한 x의 기댓값은 0이지만 실제로 실행시켜보면 그렇지 않음.
두 개의 thread가 동시에 접근해서 각자의 작업을 하지만, 메모리의 누수로인한 다른 결과가 나옴

태초에 파이썬에서 GIL이 탄생하게된 이유는 파이썬에 thread라는 개념이 없었을 시기에, 위와 같은 메모리 관리에 대한
가장 현실적인 방안이 GIL이었음. CExtension의 새로운 메모리 관리방법에 맞춰서 파이썬에 적용할 수 없었기 때문.

파이썬 개발자 명언
>I’d welcome a set of patches into Py3k only if the performance for a single-threaded program (and for a multi-threaded but >I/O-bound program) does not decrease.
>단일 thread 프로그램에서의 성능을 저하시키지 않고 GIL의 문제점을 개선할 수 있다면, 나는 그 개선안을 기꺼이 받아들일 것이다.
>하지만 여태까지 이에 대해 받아들여진 개선안은 없음.

파이썬에서도 멀티쓰레드를 통한 병렬처리 보다는 멀티프로세싱을 통한 병렬처리를 더 권장하는것 같음.
멀티프로세싱 역시 멀티쓰레드와 사용이 비슷해 이식이 비교적 쉬우며 context switching 관련 자원의 소모를 감안해야 한다.

```python
from multiprocessing import Process, Queue

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return

if __name__ == "__main__":
    START, END = 0, 100000000
    result = Queue()
    th1 = Process(target=work, args=(1, START, END//2, result))
    th2 = Process(target=work, args=(2, END//2, END, result))
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp
    print(f"Result: {total}")
```

## Rerence
https://dgkim5360.tistory.com/entry/understanding-the-global-interpreter-lock-of-cpython
https://realpython.com/python-gil/
https://bodyvisionmedical.com/articles/why-is-python-so-slow-tackling-pythons-performance-issues
https://realpython.com/python-gil/
https://ssungkang.tistory.com/entry/python-GIL-Global-interpreter-Lock%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C
https://sungmin-joo.tistory.com/11
https://monkey3199.github.io/develop/python/2018/12/04/python-pararrel.html



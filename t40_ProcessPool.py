from concurrent.futures import ProcessPoolExecutor
import time

def sq_num(num):
    time.sleep(2)
    return f"Square : {num*num}"
number = [1,2,3,4,5,6,7,8,9]

if __name__ == "__main__":
    t = time.time()
    with ProcessPoolExecutor(max_workers=3) as sourav:
        work = sourav.map(sq_num,number)
    for data in work:
        print(data)
    tt= time.time()-t
    print(tt)

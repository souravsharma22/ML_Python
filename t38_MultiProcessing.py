import multiprocessing
import time

def sq_num():
    for i in range(5):
        print(f"Square : {i*i}")
        time.sleep(1)
def cube_num():
    for i in range(5):
        print(f"Cube : {i*i*i}")
        time.sleep(1.5)

if __name__=="__main__":
    p1 = multiprocessing.Process(target=sq_num)
    p2 = multiprocessing.Process(target=cube_num)
    t= time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    comp_time = time.time()-t
    print(comp_time)
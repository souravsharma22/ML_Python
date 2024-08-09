#now lets make first loop slow
import threading
import time
def Print_num():
    for i in range(5):
        print(f"Number :{i}")
        time.sleep(2)
def print_letter():
    for let in "abcdefgh":
        print(f"Letter :{let}")
        time.sleep(1)

t = time.time()
Print_num()
print_letter()
exec_time = time.time()-t
print(exec_time)

# now lets use multithreading and do it again
t1= threading.Thread(target=Print_num)
t2= threading.Thread(target=print_letter)
tim= time.time()
t1.start()
t2.start()

t1.join()
t2.join()
runtime = time.time()-tim
print(runtime)
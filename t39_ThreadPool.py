from concurrent.futures import ThreadPoolExecutor
import time

def print_num(num):
    time.sleep(1)
    return f"number : {num}"

numbers = [1,2,3,4,5,6,7,8,9]
t = time.time()
with ThreadPoolExecutor (max_workers=3) as executor:
    working = executor.map(print_num,numbers)
for data in working:
    print(data)
tt = time.time()-t
print(tt)

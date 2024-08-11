import multiprocessing
import math
import multiprocessing.pool
import time
import sys

#for calculating very large numbers we need to increase number of operating digits
sys.set_int_max_str_digits(100000)
def calculate_factorial(num):
    print(f"Factorial of {num } is")
    fac = math.factorial(num)
    print(fac)
    return fac
if __name__ =="__main__":
    numbers =[3000,4000,6000,8000]
    start_time = time.time()

    # now creating multiple process to complete the quickly
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_factorial,numbers)
    total_time = time.time()-start_time
    print(f"Results are :{results}")
    print(f"Time Taken in process is :{total_time}")
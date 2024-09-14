from functools import lru_cache
import time
#caching is uded for memoization of reapeated tasks only for single run
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5

print("BEFORE CACHING\n")
print(fx(20))
print("done for 20")
print(fx(5))
print("done for 5")
print(fx(3))
print("done for 6")

print("AFTER CACHING\n")
print(fx(20))
print("done for 20")
print(fx(5))
print("done for 5")
print(fx(3))
print("done for 6")

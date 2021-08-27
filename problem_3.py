from time import time
from random import randint

# 테스트케이스
import numpy as np
# N = 10 ** 10
N = 10 ** 6

test_case = [0] * N
for i in range(N):
    word:str = ''.join([chr(randint(44032, 55204)) for i in range(randint(50,150))])
    test_case[i] = word

# print(test_case)

# 구현
def get_item_count(words:list)->dict:
  res = {}
  for i in words:
    try: res[i] += 1
    except: res[i] = 1
  return res

def filter_over_two(a:dict)->list:
    return list((key,value) for key, value in a.items() if value > 1)

# 출력
start = time()
answer = filter_over_two(get_item_count(test_case))
if answer:
  for word, cnt in answer:
    print(f"\"{word}\" 문장이 {cnt}번 중복됩니다.")
else:
  print(f"중복되는 문장이 없습니다.")
  
print(f"수행시간 : {time() - start}sec")
    

from tqdm import tqdm

import time
import random

people_names = ["John", "Jane", "Jack", "Jill"]

[print(name) for name in tqdm(people_names, desc="People names")]

for i in tqdm(range(10000), desc="Basic loop"):
    time.sleep(0.01)

'''
If you want to use tqdm with a while loop, you can do it like this:
'''
# progress = tqdm(total=100)
# while True:
#     time.sleep(0.1)
#     progress.update(1)
#     if random.randint(1,100) == 1:
#         break
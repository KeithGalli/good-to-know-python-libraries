from tqdm import tqdm
import random

import time

for i in tqdm(range(100)):
    time.sleep(0.25)

progress = tqdm(total=100)
while True:
    progress.update(1)
    time.sleep(0.1)
    if random.randint(1, 100) == 1:
        break
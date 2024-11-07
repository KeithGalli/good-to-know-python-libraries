from tqdm import tqdm

import time
import random

# dog_types = ['beagle', 'labrador', 'german shepherd', 'bulldog', 'poodle']

# # for dog in tqdm(dog_types, desc='Processing dog types'):
# #     # Execute
# #     time.sleep(1)

# [x.capitalize() for x in tqdm(dog_types)]

pbar = tqdm(total=100)
while True:
    pbar.update(1)
    time.sleep(0.1)
    if random.randint(1,100) == 1:
        break
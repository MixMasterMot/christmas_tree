import os
import random
import time

tree = list(open("tree3.txt").read().rstrip())

colorsList = [f'\033[91m☆\033[0m', '\033[92m☆\033[0m', f'\033[93m☆\033[0m', f'\033[94m☆\033[0m', '☆']

lights = []
for i, c in enumerate(tree):
        if c == "S":
            lights.append(i)

while True:
    
    for i in lights:
        tree[i] = colorsList[random.randint(0,4)]

    print(''.join(tree))
    
    time.sleep(random.uniform(.5, 1.5))
    os.system('cls' if os.name == 'nt' else 'clear')
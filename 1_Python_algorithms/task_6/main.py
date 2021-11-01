import random
import time

def get_one_genom():
    DATA = 'ACGT'
    return random.choice(DATA)


cg_count = 0

genom = [get_one_genom() for i in range(1000000)]

left = random.randint(10,1000)

right = random.randint(100,200) + left

start = time.time()
#1 вариант
for i in range(left, right+1):
    if genom[i] == 'C' or genom[i] == 'G':
        cg_count += 1

print(cg_count)
print(time.time() - start)


start = time.time()

#2 вариант
temp_sums = [0]
cg_count = 0


for i in range(len(genom)):
    if genom[i] == 'C' or genom[i] == 'G':
        cg_count += 1
    temp_sums.append(cg_count)



print(temp_sums[right+1] - temp_sums[left])
print(time.time() - start)

input()
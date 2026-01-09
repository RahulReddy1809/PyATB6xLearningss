# Skip numbers divisible by 3 -- range from 1 to 100

for i in range(1,100):
    if i % 3 ==0:
        continue
    print(i)
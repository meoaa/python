counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):
    for i in range(2, ptr):
        counter+=1
        if n % prime[i] == 0:
            break
    else: #정상적으로 루트가 끝났을 때 실행되는 for - else
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])

print(f'나눗셈을 한 횟수{counter}')
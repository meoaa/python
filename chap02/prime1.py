counter = 0

for n in range(2, 1001):
    for i in range(2, n):
        counter+=1
        if n % i == 0:
            break
    else: #정상적으로 루트가 끝났을 때 실행되는 for - else
        print(n)

print(f'나눗셈을 한 횟수{counter}')
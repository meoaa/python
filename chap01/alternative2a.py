print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?'))

for _ in range(1, n // 2 + 1):
    print('+-', end='')


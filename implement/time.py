n = int(input())
cnt = 0

for i in range(n+1):                            # 시 단위
    for j in range(60):                         # 분 단위
        for k in range(60):                     # 초 단위
            time = str(i) + str(j) + str(k)     # 시간 문자화
            print(time)
            if '3' in time:
                cnt += 1

print(cnt)
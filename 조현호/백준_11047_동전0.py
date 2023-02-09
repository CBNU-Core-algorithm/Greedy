import sys

# 그리디 알고리즘 문제로, 배수로 이루어진 동전의 가치로 인해서 그리디로 풀 수 있습니다.
# 그냥 순서대로 그 순간 최적의 답을 선택해 계산을 해 나가면 오류없이 답이 나오도록 설계된 문제입니다.
# ex) 800 / 500, 400, 100 이런 경우에는 그리디로 풀지 못하겠죠.

sys.stdin = open('a.txt', 'rt') # 테스트용 코드
input = sys.stdin.readline

# 값 입력 받기
n, k = map(int, input().strip().split())
# coin_list = [int(input()) for _ in range(n)]
coin_list = []
for i in range(n):
    coin_list.append(int(input()))

# 정답 저장을 위한 글로벌변수 만들기
ans = 0

# 코인을 내림차순으로 만들고 순서대로 거스름돈과 비교
for coin in coin_list[::-1]:
    # 거스름돈이 0이면 빠져나오기
    if k == 0:
        break

    if k >= coin:
        # 건네준 코인 개수를 답에 더하기
        ans += k // coin
        # k에 남은 거스름돈을 재할당
        k %= coin

# 정답출력
print(ans)

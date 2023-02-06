total_number, sum_worth=map(int, input().split())
coin=[int(input()) for _ in range(total_number)] #입력

coin.sort(reverse=True) #내림차순 정렬
count=0 #카운터 변수
save=0 #임시 저장 변수

for i in range(total_number):
  if(sum_worth>=coin[i]): #동전의 값이 돈보다 작다면
    save=sum_worth//coin[i] #필요한 동전의 개수
    count=count+save #카운팅
    sum_worth=sum_worth-save*coin[i] #남은 돈
    
print(count) #총 동전 개수 출력

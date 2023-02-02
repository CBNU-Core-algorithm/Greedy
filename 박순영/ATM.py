total_number=int(input()) #총 숫자 입력
time=list(map(int, input().split())) #각 숫자 입력

time.sort() #각 숫자 오름차순 정렬
sum=0 #카운팅 변수
for i in range(total_number): #[1, 2, 3]인 경우, 
    sum=sum+time[i]*(total_number-i) #1+(1+2)+(1+2+3)로 첫번째 숫자는 총 숫자 개수만큼 더해지고, 두번째 숫자는 총 숫자개수-1만큼 더해짐

print(sum)

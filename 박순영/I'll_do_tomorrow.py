total_number=int(input()) #총 숙제 수 입력
works=[]
line = []
 
for i in range(total_number):
    a, b=map(int, input().split())
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    line.append(b)
    line.append(a)     # 마감날짜, 소요기간 순으로 리스트 입력
    works.append(line) 

works=sorted(works, key=lambda work: work[0], reverse=True) #리스트 마감날짜순으로 내림차순 정렬
sub=works[0][0]-works[0][1] #제일 마지막 마감 날짜에서 소요기간 빼기
for j in range(1, total_number): #반복
    if(sub>works[j][0]):
      sub=works[j][0]-works[j][1]
    else: #sub<=works[j][0]
      sub=sub-works[j][1]
print(sub) #최종 시작 날짜 나옴

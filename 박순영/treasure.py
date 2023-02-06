N=int(input())
A=list(map(int, input().split())) 
B=list(map(int, input().split())) #입력
A.sort() #오름차순 정렬

result=0 #결과값 저장 변수
for i in range(N):
  max_numberB=B.index(max(B)) #B최댓값 인덱스
  result+=A[i]*B[max_numberB] #A최솟값*B최댓값
  B.pop(max_numberB) #계산한 요소 빼냄
print(result)#결과 출력

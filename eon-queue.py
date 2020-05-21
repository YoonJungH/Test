case = int(input("입,출력 경우의 수 :"))
for _ in range(case):
 n, m = list(map(int, input("작업 수/작업 번호 :").split()))
 priority = list(map(int,input("작업 우선순위 :").split()))
 print_num = list(range(len(priority)))
 print_time = 0                           #초기시간은 0으로 지정

 while True :
   if priority[0] == max(priority):        #우선 순위가 가장 높을 때
      print_time += 1                      #우선 순위가 가장 높을 떈 바로 인쇄
      if print_num[0] == m:
          print(print_time,"분")
          break
      else:                       
          print_num.pop(0)
          priority.pop(0)
   else:                                   #우선 순위가 제일 높지 않을 때
       priority.append(priority.pop(0))
       print_num.append(print_num.pop(0))





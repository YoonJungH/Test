snail = int(input("수를 입력하세요:"))
data = [[0] * snail for i in range(snail)] 

column = 0   #행(세로)
row = -1     #열(가로)
number = 0   #수
way = 1      #방향

def recur(column,row,number,way,snail): 
    
    for a in range(1,snail + 1): 
        number = number + 1 
        row = row + way
        data[column][row] = number  
    snail = snail - 1  
    for a in range(1,snail + 1): 
        number = number + 1 
        column = column + way 
        data[column][row] = number     
    way = way * -1
    if snail == 0 : 
        return 0 

    return recur(column,row,number,way,snail)   #재귀함수
recur(column,row,number,way,snail)              #함수호출
for column in range(snail):
    print(data[column])
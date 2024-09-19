n = int(input())

lis = []

stt = list(map(int,input().split()))


for i in range(0,n*2,2):
    lis.append([stt[i],stt[i+1]])



# def tedekhol(e1,e2):
#     if e1[0] > 


lis.sort(key=lambda x: x[1])

# print(lis)


posible_games = []

posible_games.append(lis[0])

for i in range(1,len(lis)) :
    if posible_games[-1][1] <= lis[i][0]:
        posible_games.append(lis[i])
        
        
print(len(posible_games))
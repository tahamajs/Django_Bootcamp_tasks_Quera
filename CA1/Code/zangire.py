shekari_team = [0,0]
namaki_team = [9,9]

n = int(input())




def kharej(team):
    return team[0] < 10 and team[0] >= 0 and team[1] < 10 and team[1] >= 0



winer = -1 
# draw = -1
# shekari = 1
# namaki = 2


for i in range(n):
    
    
    order = input()
    
    if winer != -1:
        continue
    
    
    
    if order == 'r':
        if i%2 == 0 :
            #shekari
            shekari_team[0] += 1
            if not kharej(shekari_team):
                winer = 2
            if shekari_team == namaki_team :
                winer = 2
        else:
            namaki_team[0] += 1
            if not kharej(namaki_team):
                winer = 1
            if shekari_team == namaki_team :
                winer = 1
                
                
                
                
                
                
    elif order == 'l':
        if i%2 == 0 :
            #shekari
            shekari_team[0] -= 1
            if not kharej(shekari_team):
                winer = 2
            if shekari_team == namaki_team :
                winer = 2
        else:
            namaki_team[0] -= 1
            if not kharej(namaki_team):
                winer = 1
            if shekari_team == namaki_team :
                winer = 1
                
                
                
    elif order == 'u':
        if i%2 == 0 :
            #shekari
            shekari_team[1] -= 1
            if not kharej(shekari_team):
                winer = 2
            if shekari_team == namaki_team :
                winer = 2
        else:
            namaki_team[1] -= 1
            if not kharej(namaki_team):
                winer = 1
            if shekari_team == namaki_team :
                winer = 1
                
                
                
                
                
    elif order == 'd':
        if i%2 == 0 :
            #shekari
            shekari_team[1] += 1
            if not kharej(shekari_team):
                winer = 2
            if shekari_team == namaki_team :
                winer = 2
        else:
            namaki_team[1] += 1
            if not kharej(namaki_team):
                winer = 1
            if shekari_team == namaki_team :
                winer = 1
            
            
            
            
            
            
            
            



    elif order == 'sr':
        if i%2 == 0 :
            #shekari
            if shekari_team[1] == namaki_team[1] and shekari_team[0] > namaki_team[0]:
                winer = 1
        
        else:
            if shekari_team[1] == namaki_team[1] and shekari_team[0] < namaki_team[0]:
                winer = 2
                
                
                
                
                
    elif order == 'sl':
        if i%2 == 0 :
            #shekari
            if shekari_team[1] == namaki_team[1] and shekari_team[0] < namaki_team[0]:
                winer = 1
        
        else:
            if shekari_team[1] == namaki_team[1] and shekari_team[0] > namaki_team[0]:
                winer = 2
                
                
                
                
    elif order == 'su':
        if i%2 == 0 :
            #shekari
            if shekari_team[0] == namaki_team[0] and shekari_team[1] > namaki_team[1]:
                winer = 1
        
        else:
            if shekari_team[0] == namaki_team[0] and shekari_team[1] < namaki_team[1]:
                winer = 2
                
                
                
                
    elif order == 'sd':
        if i%2 == 0 :
            #shekari
            if shekari_team[0] == namaki_team[0] and shekari_team[1] < namaki_team[1]:
                winer = 1
        
        else:
            if shekari_team[0] == namaki_team[0] and shekari_team[1] > namaki_team[1]:
                winer = 2
    
    
    
# print(shekari_team,namaki_team , winer )

if winer == 1:
    print("shekaria won")
elif winer == 2:
    print ("namakia won")
elif winer == -1:
    print("draw")
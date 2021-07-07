import random
num = random.randint(1,20)
y=0
while (y < 5):    
    x=input('輸入數字')
    x=int(x)  
    if x > num:   
        print('數字太大囉!')       
    elif x < num:    
        print('數字太小囉!')        
    else :    
        print('答對囉! 你花費' + str(y) + '次機會')
        break
    y += 1
  
if y>=5 :
   print('哈哈, 失敗囉!')
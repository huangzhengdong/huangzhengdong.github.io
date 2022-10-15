"""python小游戏"""
import random
answer=random.randint(1,10)
counts=3
while counts>0:
    temp=input("猜猜我心里想的数字")
    guess=int(temp)
    if guess==answer:
        print("你猜对了")
        break
    else :
        if guess>answer:
            print("大了")
        else :
            print("小了")
    counts=counts-1
print("游戏结束")

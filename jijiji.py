"""用python设计第一个游戏"""
import random
answer=random.randint(1, 10)
counts=3
while counts>0:
    temp=input("不妨猜一下小甲鱼现在心里想的是哪个数字")
    guess=int(temp)
    if guess==answer:
        print("恭喜你猜对了")
        break
    else :
        if guess>answer:
            print("大了")
        else:
            print("小了")
    counts=counts-1
print("游戏结束，不玩了")
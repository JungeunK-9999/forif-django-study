import random
import time

AI = 0
PLAYER = 0

def convert(number):
    if number == 1:
        return "가위"
    elif number == 2:
        return "바위"
    elif number == 3:
        return "보"

def game():
    robot = random.randint(1,3)
    choice = int(input("1.가위 2.바위 3.보  >>> "))
 
    print("두구두구두구두구두구...결과는..?!")
    time.sleep(0.2)
    print(f"robot: {convert(robot)}")
    print(f"you: {convert(choice)}")
    time.sleep(0.1)

    if robot == 1 and choice == 3:
        robot = 4
    if robot == 3 and choice == 1:
        choice = 4
    
    if robot>choice:
        print("로봇이 이겼습니다.")
        global AI
        AI += 1
    elif robot<choice:
        print("당신이 이겼습니다.")
        global PLAYER
        PLAYER+=1


    print(f"로봇 {AI} : 당신 {PLAYER}")
    print()

    
while AI<3 and PLAYER<3 :
    game()

if AI>PLAYER:
    print("로봇 승리!")
else:
    print("플레이어 승리!")

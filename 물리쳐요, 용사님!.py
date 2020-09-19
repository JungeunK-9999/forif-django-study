# 물리쳐요 용사님!
import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.atk = random.randint(50,200)
        self.gold = 1000

    def get_item(self):
        self.gold -= 200
        self.atk += random.randint(15,30)

    def checking(self):
        print()
        print(f"--------{self.name}님의 현재상태--------")
        print("gold:", self.gold)
        print("공격력:", self.atk)
        
class Monster:
    def __init__(self):
        self.atk = random.randint(30,250)

def greeting():
    name = input("용사님의 이름을 알려주세요 : ")
    hero = Hero(name)
    hero.checking()
    return hero

def meeting_monster(hero):
    monster = Monster()
    if hero.atk>monster.atk:
        print("몬스터를 물리쳤습니다!")
        hero.atk -= 10
    elif hero.atk<monster.atk:
        print("몬스터에게 패배했습니다.")
        hero.atk += 10
    else:
        print("몬스터와 열심히 싸웠지만 물리치지 못하였습니다...")
        hero.atk -= 10

def start():
    global hero
    hero = greeting()

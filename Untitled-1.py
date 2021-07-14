#제곱은 ** | pow(a,b)
#or 과 and 는 각각 |,&
#최댓값은 max(a,b) 최소값은 min(a,b)
#반올림은 round(a)
#floor sqrt ceil 은 from math import* 를 했을때 각각 내림, 제곱근, 올림 으로 사용가능
#from random import* 을 하면 random ,randrange , randint 사용가능 
#random은 0.0 이상 1.0 미만의 임의의값

#score_file = open("score.txt","w",encoding=utf8)
# print("수학 :0",file=score_file)
# printf("영어 :50",file=score_file)
# score_file.close()

# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학:80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file =open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file =open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end="") #줄별로 읽기,한줄읽고 커서는 다음줄
# print(score_file.readline())

# score_file =open("score.txt","r",encoding="utf8")
# # while True:
# #     line = score_file.readline()
# #     if not line:
# #         break
# #     print(line,end="")
# # score_file.close()

# lines=score_file.readlines()
# for line in lines:
#     print(line,end="")
     
# score_file.close()

import pickle
# profile_file =open("profile.pickle","wb")
# profile ={"이름 ":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file)
# profile_file.close()


# profile_file =open("profile.pickle","rb")
# profile =pickle.load(profile_file)
# print(profile)
# profile_file.close()


# with open("profile.pickle","rb")as profile_file:
#     print(pickle.load(profile_file))

# with open("test.txt", "w", encoding="utf8") as test_file:
#     test_file.write("아아 파이썬공부중")

#with open("test.txt","r",encoding="utf8") as test_file:
 #       print(test_file.read())



# for i in range(1,51):
#     with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
#         report_file.write(str(i)+"주차 주간보고")
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")    



# name = "마린"
# hp =40
# damage = 5

# print("{}유닛이 생성 되었습니다.".format(name))
# print("체력 {0},공격력 {1}\n".format(hp,damage))


# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{}유닛이 생성 되었습니다.".format(tank_name))
# print("체력 {0},공격력 {1}\n".format(tank_hp,tank_damage))

# def attack(name,location,damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다.\
#     [공격력 {2}]".format(name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)

class unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))


    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name,location,self.speed))

    def damaged(self,damage):
        print("{0} :{1} 데미지를 입었습니다."\
        .format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name)) 


# marine = unit("마린",40,5)
# marine2 = unit("마린",40,5)
# tank = unit("탱크",150,35)

# wraith1 = unit("레이스",85,5)
# print("유닛이름 : {0},공격력 : {1}".format(wraith1.name,wraith1.damage))

# wraith2 = unit("레이스",80,5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))

class attackunit(unit):
    def __init__(self, name, hp, speed, damage):
        unit.__init__(self,name,hp,speed)  
        self.damage = damage    
        print("{0}유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
   
    def attack(self,location):
        print("{0}:{1}방향으로 적군을 공격 합니다.[공격력 : {2}"\
            .format(self.name,location,self.damage))
   
    def damaged(self,damage):
        print("{0} :{1} 데미지를 입었습니다."\
        .format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name)) 

#firebat1 = attackunit("파이어뱃",50,16)
#firebat1.attack("5시")

#firebat1.damaged(25)
#firebat1.damaged(25)

class flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed


    def fly(self,name,location):
        print(("{0} : {1} 방향으로 날아갑니다.[속도 {2}]")\
            .format(name,location,self.flying_speed))

class flyableattackunit(attackunit,flyable):
    def __init__(self,name,hp,damage,flying_speed):
        attackunit.__init__(self,name,hp,0,damage) #지상 speed 0
        flyable.__init__(self,flying_speed)

    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

vulture = attackunit("벌쳐",80,10,20)
battlecruiser = flyableattackunit("배틀크루저",500,25,3)

vulture.move("11시")
battlecruiser.move("9시")

# class buildingunit(unit):
#     def __init__(self,name,hp,location):
#         unit.__init__(self,name,hp,0)
#         super().__init__(name,hp,0)
#         self.location = location

#supply_depot = buildingunit("서플라이 디폿",500,"7시")

#def game_start():
 #   print("[알림] 새로운 게임을 시작합니다.")

#def game_over():
 #   pass

#game_start()
#game_over()

class marine(attackunit):
    def __init__(self):
        attackunit.__init__(self,"마린",40,1,5)
    def stimepack(self):
        if self.hp> 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소"\
                .format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩 사용이 불가합니다."\
                .format(self.name))        
class tank(attackunit):
    seize_developed = False #시즈모드 개발여부

    def set_seize_mode(self):
        if tank.seize_developed == False:
            return

        #현재 시즈모드 아닐 때
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다."\
                .format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #현재 시즈모드 일 때
        else:print("{0} : 시즈모드를 해제합니다."\
                .format(self.name))
            self.damage /= 2
            self.seize_mode = False
        

    def __init__(self):
        attackunit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False

class wraith(flyableattackunit):
    def __init__(self):
        flyableattackunit.__init__(self,"레이스",80,20,5)
        self.clocked = False #클로킹모드 (해제상태)

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹모드를 해제합니다"\
                .format(self.name))
        else:      
            print("{0} : 클로킹 모드 설정합니다."\
                .format(self.name))
            self.clocked = True      






























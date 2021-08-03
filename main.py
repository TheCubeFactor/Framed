import time
from random import randint

print("Welcome to...")
time.sleep(5)
print("FRAMED")

Gl = 1


def ran():
    ran_num = randint(0, 1)
    print("Random 0 or 1")


def death():
    print("Game Over!")
    start()


def start():
    GL = 1
def level_2():
    print("You must remember your past... and figure out what happend")
    time.sleep(5)
    print("Level 2")
    time.sleep(4)
    print("A path down memory lane")

def level_1():
    print("Hello...")
    time.sleep(1)
    print("Do You... Hear me?")
    time.sleep(3)
    print("You say yes")
    time.sleep(4)
    print("There is no time come QUICK")
    time.sleep(5)
    print("You are knocked out and wake up in a prison...")
    time.sleep(2)
    print("You Must Escape and prove that you were...")
    time.sleep(5)
    print("FRAMED")
    time.sleep(5)
    print("Level 1")
    time.sleep(4)
    print("Awake")
    time.sleep(1)
    choose = input("You see a small metalic Object... Take it? Y or N")
    if choose == "Y" or "y":
        time.sleep(0.65)
        print("You Grab it")
        #lock picking part
        time.sleep(1)
        choose = input("You think about it and bend the object then you relise You can pick the lock! Do  you do it? Y or N")
        if choose == "Y" or "y":
            time.sleep(1)
            print("You poke and point and with a lot of luck... You Open it!!!")
            time.sleep(1)
            print("But wait you hear guards coming")
            time.sleep(1)
            death()
        else:
            time.sleep(1)
            print("You stop and think the memory's you had fading...")
            time.sleep(1)
            print("The one memory... Someone framed you for this...")
            #nex lev



    else:
        time.sleep(1)
        print("You Leave it down")
        #Non lock picking
        print("the guards come and lock you up in the new cell... Forever")
        time.sleep(1)
        death()












def game():
    start()
    level_1()


game()

print("welcome to my first game")
name=input("what is your name ")
age=int(input("what is your age "))
print("hello",name,"you are",age ,"years old.")


health=10

if age >= 18:
    print("you are old enough to play")
    wants_to_play=input("you want to play? ").lower()
    if (wants_to_play=="yes"):
        print("Lets play!")
        print("you are starting with", health, "health")
        left_or_right=input("your first choice...  left or right (left/right)? ")
        if left_or_right=='left':
            ans=input("Nicee..you have reached a lake ..do you want to swim across or "
                      "go around (across/ around)? ")
            if ans=="around":
                print("you went around and reached other side of the lake")
            elif ans=="across":
                print("you managed to get across,but were bit by a fish and lost 5 health")
                health-=5


            ans=input("you notice a house and a river which do you go to (river/house)? ")
            if ans=="house":
                print("you go to the house and greeted  by the owner...he doesnt like"
                      " u and you loose 5 health")
                health-=5

                if health<=0:
                    print("you have 0 health and you lost the game...")
                else:
                    print("you have survived ..you win!!!")
            else :
                print("you fell in the river you lost..")


        else:
            print("you fell down and lost")
    else :
                print("you lose")


else :
    print("you are not old enough to play")

import random
balls=6*int(input("Enter The Numbers of Over you want play: "))
opt=[0,1,2,4,6]
print("You will have 2 wickets Choose valid option from the list {0,1,2,4,6}")
ball,wicket,score=0,0,0
batsman=[]
bowler=[]
while(ball<balls):
    bats=int(input("Enter Your Choice:"))
    while bats not in opt:
        print("Enter valid Run")
        bats=int(input("Enter Your Choice:"))
    bowl=random.choice(opt)
    print(f"Bowler :{bowl}")
    if bats==bowl:
        wicket+=1
        batsman.append("x")
        bowler.append(wicket)
    else:
        if wicket==0:
            score+=bats
            batsman.append(bats)
            bowler.append("-")

        else:
            score+=bats
            batsman.append(bats)
            bowler.append(wicket)
    ball+=1
    if wicket==2:
        print("Game Over!")
        break

print("Score Card")
print(" Batsman\t\t  Bowler")
for i in range(ball):
    print(f"\t{batsman[i]}\t\t\t\t{bowler[i]}")
print("Your Total Score: ")
print(f"You have Played {ball} Balls")
print(f"Runs={score}   Wicket={wicket}")
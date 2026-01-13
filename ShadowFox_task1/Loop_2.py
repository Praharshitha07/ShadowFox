#Jumping jacks workout program 
Total_jumping_jacks=100
completed=0
# performing jumping jacks in sets of 10
for i in range(10):
    completed+=10
    print("Completed", completed, "jumping jacks")
    remaining=Total_jumping_jacks - completed
    tired=input("Are you tired(yes/y or no/n)? ").lower() #asking user if they are tired
    if tired=="yes" or tired=="y":
        skip=input("Do you want to skip remaining jumping jacks(yes/y or no/n)? ").lower()
        if skip=="yes" or skip=="y":
            print("you have completed a total of", completed, "jumping jacks. Good job!")
            break
        else:
            if remaining>0:
                print(remaining, "jumping jacks remaining. ")
if completed==Total_jumping_jacks:
    print("congratulations! you completed the workout")                


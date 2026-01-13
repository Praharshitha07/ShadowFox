#Loops 
#1.Dice Rolling Simulation
import random
count_6=0
count_1=0
couont_two_sixes=0
previous_roll=0 # to track the previous roll for consecutive sixes
#Roll the die 20 times 
for i in range(20):
    roll=random.randint(1,6) #generate random number between 1 and 6
    print("Roll", i+1, ":", roll)
    #count number of times 6 is rolled
    if roll==6:
        count_6+=1
        #check for consecutive sixes
        if previous_roll==6:
            couont_two_sixes+=1
    #count number of times 1 is rolled
    if roll==1:
        count_1+=1
    previous_roll=roll #update previous roll
#printinf results
print("Total number of times 6 was rolled:", count_6)
print("Total number of times 1 was rolled:", count_1)   
print("Total number of times two consecutive sixes were rolled:", couont_two_sixes)


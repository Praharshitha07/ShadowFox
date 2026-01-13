
#initial Justrice Lists
justice_league = ["Superman", "Batman","Wonder Woman", "The Flash", "Aquaman", "Green Lantern"]

#1. calculate the number of members in the Justice League
num_members = len(justice_league)
print("Number of members in the Justice League:", num_members)

#2. Add Batgirl and Nightwing to the Justice League
new_members = ["Batgirl", "Nightwing"]
justice_league.extend(new_members)
print("Updated Justice League members after adding Batgirl and Nightwing:", justice_league)

#3.Make Wonder Woman the team leader by moving her to the first position in the list
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Justice League members after making Wonder Woman the team leader:", justice_league)

# 4. seperate Aquaman and Flash 
#moving Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")      
justice_league.insert(justice_league.index("Aquaman") + 1, "Green Lantern")
print("Justice League members after separating Aquaman and Flash:", justice_league)

#5. replace entire Justice League with new team 
justice_league=["Cyborg", "Shazam", "Hawkgirl","Martian Manhunter","Green Arrow"]
print("Justice League members after replacing with new team:", justice_league)

#6. Sort the Justice League members in alphabetical order
justice_league.sort()
print("Justice League members in alphabetical order:", justice_league)

#7. new leader 
print("New team leader is:", justice_league[0])


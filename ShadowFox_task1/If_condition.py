#1. BMI category program 
height=float(input("enter height in meters:"))
weight=float(input("enter weight in kilograms:"))

#calculate BMI
bmi=weight/(height**2)
print("Your BMI is:", round(bmi,2))
#determine BMI category
if bmi>=30:
    print("Obesity")
elif bmi>=25:
    print("Overweight")
elif bmi>=18.5:
    print("Normal")
else:
    print("Underweight")

#2. find country of a city 
Australia =["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE=["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India=["Mumbai","Banglore","Chennai","Delhi"]
#input of city name 
city=input("enter city name:")
#determine country of the city
if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")
else:
    print("City not found")

#3. checking if two cities belong to same country
Australia =["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE=["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India=["Mumbai","Banglore","Chennai","Delhi"]
#input of two city names
city1=input("enter first city name:")
city2=input("enter second city name:")
#determine if both cities belong to same country
if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")
elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")
elif city1 in India and city2 in India:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")


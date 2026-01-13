#1. function using format() method 
def format_number(num, fmt):
    return format(num, fmt) #format() method converts the number based on the given format 
# Example usage:
result = format_number(145, 'o')  # Convert to octadecimal
print("formatted number is:", result)

# 2. Area of circular pond and water calculation
radius = 84 # radius in meters
Area= 3.14 * radius * radius # Area of circle formula
print("Area of circular pond is:", Area, "square meters")
liters_per_square_meter = 1.4 
total_liters = Area * liters_per_square_meter
print("total amount of water in the pond is:", int(total_liters), "liters")

#3. speed calculation
distance = 490 # distance in meters
time_minutes = 7 # time in minutes
time_seconds = time_minutes * 60 # converting time to seconds   
speed = distance / time_seconds # speed in meters per second
print("speed of the object is:", int(speed), "meters/second")#print speed without decimal points




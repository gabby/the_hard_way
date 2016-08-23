#this function defines how many total available cars there are
cars = 100
#this function defines the total capacity of each car
space_in_a_car = 4.0
#this function defines how many drivers there are
drivers = 30
# this function defines how many passengers there are
passengers = 90
#this function will return the number of empty cars by subtracting the number drivers to the total number of cars
cars_not_driven = cars - drivers
#this function is equal to an already defined function drivers, but indicates how many available cars there are since every car needs at least one driver. 
cars_driven = drivers
#this function determines the total number of passengers can be transported that day 
carpool_capacity = cars_driven * space_in_a_car
#given the number of passengers that day and the number of available cars, this function returns the number of passengers we need to put in each car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
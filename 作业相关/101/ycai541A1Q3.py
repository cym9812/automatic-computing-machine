"""
Name: Yimeng Cai
username: ycai541
ID number: 455251836
Description: Calculates the minimum number of vehicles required to
             transport a given number of passengers,and the cost of
             transporting that number of passengers.
"""
Number_of_people = int(input("Number of people: "))
print()
shuttles = Number_of_people // 20
vans = (Number_of_people - shuttles * 20) // 9
cars = (Number_of_people - shuttles * 20 - vans * 9) // 4
motorcycles = Number_of_people - shuttles * 20 - vans * 9 - cars * 4
total_cost = shuttles * 85 + vans * 45 + cars * 25 + motorcycles * 15
print("You will need:")
print("=" * 19)
print("  Shuttles: ", shuttles, sep="")
print("  Vans: ", vans, sep="")
print("  Cars: ", cars, sep="")
print("  Motorcycles: ", motorcycles, sep="")
print()
print("Total cost: $", total_cost, sep="")
print("=" * 19)
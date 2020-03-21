def get_worst_manufacturer_dict(filename):
    car_file = open(filename, "r")
    car_data = {}
    for each_line in car_file:
        data = each_line.split()
        if data[1] not in car_data:
            car_data[data[1]] = data[0:1]
        else:
            car_data[data[1]] = car_data[data[1]] + data[0:1]
    return car_data

car_dict = get_worst_manufacturer_dict('cars_simple.txt')
for key in sorted(car_dict):
    print(key, ':', car_dict[key])
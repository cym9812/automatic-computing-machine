def print_worst_manufacturer(car_dict):
    most = 0
    most_brand = ""
    for brand in car_dict:
        if len(car_dict[brand]) > most:
            most_brand = brand
            most = len(car_dict[brand])
    print("Worst manufacturer:", most_brand)

car_dict = {'Amphicar': ['1961'], 'Corvair': ['1961'], 'Horsey': ['1899'], 'Overland': ['1911'], 'Ford': ['1909', '1958']}
print_worst_manufacturer(car_dict)
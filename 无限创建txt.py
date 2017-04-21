file_name = 0
while file_name<10000:
    file_name = file_name + 1
    full_name = str(file_name) + ".txt"
    open(full_name,"w")

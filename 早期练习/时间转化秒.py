def get_seconds(time):
    hours = int(time[:time.find(":")])*60*60
    minutes = int(time[time.find(":")+1:time.rfind(":")])*60
    seconds = int(time[time.rfind(":")+1:-1])
    total_seconds = hours+minutes+seconds
    return total_seconds

def main():
    time1 = "02:04:56"
    print(time1, "is", get_seconds(time1), "seconds")
    time2 = "09:48:24"
    print(time2, "is", get_seconds(time2), "seconds")
main()
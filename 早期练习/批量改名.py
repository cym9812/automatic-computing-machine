import os

number = 1

def change_name(current_file, new_file):
    print(current_file)
    print(new_file + '\n')
    try:
        os.rename(current_file, new_file)
    except:
        pass

while number < 25:
    file_to_change = "[VCB-S]Toaru Majutsu no Index II[0"+ str(number) + "][Hi10p_1080p][BDRip][x264_2flac].ass"
    new_file = "[VCB-Studio] Toaru Majutsu no Index II [0"+ str(number) + "][Hi10p_1080p][x264_2flac].ass"
    change_name(file_to_change, new_file)
    number += 1
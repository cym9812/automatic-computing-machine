######################################
#   COMPSCI 105 S2 C, 2017           #
#   Assignment 2 Question 1          #
#                                    #
#   @author:     Yimeng Cai, Ycai541 #
#   @version:    19/10/2017          #
######################################
class Team:
    def __init__(self, name, conference, points, goals_for, goals_against):
        self.__name = name # the team name
        self.__conference = conference # the team conference
        self.__points = points  # number of points
        self.__goals_for = goals_for  # the goals for the team
        self.__goals_against = goals_against  # the goals against the team

    def get_conference(self):
        return self.__conference

    def get_points(self):
        return self.__points

    def get_goals_for(self):
        return self.__goals_for

    def get_goals_against(self):
        return self.__goals_against

    def get_difference(self):
        return  self.__goals_for - self.__goals_against

    def __str__(self):
        return '{0:<25}{1}{2:>9}{3:>7}{4:>8}:{5}'.format(self.__name, self.__conference, self.__points, self.get_difference(), self.__goals_for, self.__goals_against)


def read_data(file_name):
    data_file = open(file_name, 'r')
    data_list = data_file.read()
    data_file.close()
    data_list = data_list.split('\n')
    result = []
    for each in data_list:
        result.append(each.split(','))#Make each team's data a separate item in the list
    return result

def insertion_sort(a_list):
    for item_index in range(1, len(a_list)):
        item_to_insert = a_list[item_index]
        index = item_index - 1
        while index >= 0 and a_list[index].get_points() > item_to_insert.get_points():
            a_list[index + 1] = a_list[index]
            index -= 1
        if a_list[index].get_points() == item_to_insert.get_points():#If the points are equal
            if a_list[index].get_difference() > item_to_insert.get_difference():
                a_list[index + 1] = a_list[index]
                index -= 1
            elif a_list[index].get_difference() == item_to_insert.get_difference():
                #If the points and goal difference are equal
                if a_list[index].get_goals_for() > item_to_insert.get_goals_for():
                    a_list[index + 1] = a_list[index]
                    index -= 1
        a_list[index + 1] = item_to_insert

def print_conference(conference, team_list):
    print()
    print(' Conference ', conference)
    print('    Team                Conference Points  Diff     Goals')
    count = 1
    for each in team_list:
        if each.get_conference() == conference:
            print('{:^4}'.format(str(count) + '.'), end='')
            print(each)
            count += 1

def main():
    print("UPI: ycai541")
    print()
    data = read_data('table1.txt')
    team_list = []
    for each in data:
        team_list.append(Team(str(each[0]), int(each[1]), int(each[2]), int(each[3]), int(each[4])))
    insertion_sort(team_list)
    team_list.reverse()
    print('    Team                Conference Points  Diff     Goals')
    for i in range(len(team_list)):
        print('{:^4}'.format(str(i + 1) + '.'), end='')
        print(team_list[i])
    print()
    print_conference(1, team_list)
    print_conference(2, team_list)
    print_conference(3, team_list)
    print_conference(4, team_list)

main()

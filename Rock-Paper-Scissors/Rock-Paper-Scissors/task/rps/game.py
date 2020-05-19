import random


def run_extended_game(options_list):
    if "" in options_list:
        options_list = ['rock', 'paper', 'scissors']
    global user_score
    while True:
        user_option = input()
        if user_option in options_list:
            index_of_option = options_list.index(user_option)
            without_option = options_list[index_of_option + 1:] + options_list[:index_of_option]
            half_of_length = int(len(without_option) / 2)
            stronger_than_option = without_option[:half_of_length]
            weaker_than_option = without_option[half_of_length:]
            computer_option = random.choice(options_list)
            if computer_option in weaker_than_option:
                print(f"Well done. Computer chose {computer_option} and failed")
                user_score += 100
            elif computer_option in stronger_than_option:
                print(f"Sorry, but computer chose {computer_option}")
            else:
                print(f"There is a draw ({computer_option})")
                user_score += 50
        elif user_option == "!rating":
            print(user_score)
        elif user_option == "!exit":
            print("Bye!")
            break
        else:
            print("Invalid input")


def read_user_score(name):
    rating_file = open("rating.txt")
    ratings = rating_file.readlines()
    ratings = [line.strip().split() for line in ratings]
    ratings_dict = {}
    for el in ratings:
        ratings_dict[el[0]] = el[1]
    rating_file.close()

    if user_name in ratings_dict.keys():
        return int(ratings_dict[name])
    else:
        return 0


user_name = input("Enter your name: ")
print(f"Hello, {user_name}")
user_score = read_user_score(user_name)
op_list = input().split(",")
print("Okay, let's start")
run_extended_game(op_list)

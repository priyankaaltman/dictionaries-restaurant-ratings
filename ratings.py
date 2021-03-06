import sys


def get_user_input():

    """Get a restaurant name and score from the user."""

    new_restaurant_name = input("Choose a restaurant: ").title()
    new_restaurant_score = input("Rate that restaurant on a scale from 1 to 5: ")

    while True:

        if int(new_restaurant_score) > 5 or int(new_restaurant_score) < 1:
            print("Your rating was out of range. Please choose again.")
            new_restaurant_score = input("Rate that restaurant on a scale from 1 to 5: ")

        if 1 <= int(new_restaurant_score) <= 5:
            break

    return (new_restaurant_name, new_restaurant_score)


def list_restaurant_ratings(the_file):

    """List restaurant ratings."""

    restaurant_ratings = {}
    filename = open(the_file)
    print(filename)

    for line in filename:

        line = line.rstrip()

        item = line.split(":")

        restaurant_ratings[item[0]] = item[1]

    return restaurant_ratings


def print_alpha_ratings(the_dict):

    """Print ratings in alphabetical order."""

    tuples_list_dictionary = the_dict.items()
    in_order_tuples_list = sorted(tuples_list_dictionary)

    for restaurant, rating in in_order_tuples_list:
        print("{} is rated at {}.".format(restaurant, rating))


def master(the_file):

    """Open source file and ask user how to proceed."""

    filename = open(the_file)

    while True:
        choice = input(
            "Would you like to a) see all the ratings, b) add and rate a " + 
            "restaurant, or c) quit?: "
        )

        if "a" == choice:
            original_dict = list_restaurant_ratings(the_file)
            print_alpha_ratings(original_dict)
        elif "b" == choice:
            custom_input = get_user_input()
            update_dict = list_restaurant_ratings(the_file)
            update_dict[custom_input[0]] = custom_input[1]
            print_alpha_ratings(update_dict)
        elif "c" == choice:
            return False
        else:
            print("Please enter a, b, or c.")


master(sys.argv[1])







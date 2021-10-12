"""
Brief description ...
Name: Cue Nguyen
Date started: 05/10/2021
GitHub URL: https://github.com/JCUB-CP1404/assignment-1-kevin-aus
"""

in_file = "places.csv"

# CHOICES = 'LAMQ'


def load_places(csv_file):
    print("Loaded!")


def display_menu():
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def list_places():
    print('Choice L')


def add_new_place():
    print('Choice A')


def mark_a_place_visited():
    print('Choice M')


def main():
    print("Travel Tracker 1.0 - by Cue Nguyen")
    load_places(in_file)
    display_menu()
    choice = input("Enter a choice: ")
    choice = choice.strip().upper()

    while choice[0] != 'Q':
        if choice[0] == 'L':
            list_places()
        elif choice[0] == 'A':
            add_new_place()
        elif choice[0] == 'M':
            mark_a_place_visited()
        else:
            print("Invalid choice")
        display_menu()
        choice = input("Enter a choice: ")
        choice = choice.strip().upper()
    print("Bye.")


if __name__ == '__main__':
    main()
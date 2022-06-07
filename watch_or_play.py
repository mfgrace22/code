#!usr/bin/python3

import random
import sqlite3

movies = [
    "Without Remorse",
    "Tiger Woods Doc",
    "Army of the Dead",
    "War Pigs",
    "6 Underground",
]
shows = [
    "OITNB",
    "The Profit",
    "Hell's Kitchen",
    # "Mare of Easttown",
    "Shark Tank",
    "Naked and Afraid",
    "Flash",
    "Shadow and Bone",
]
video_games = [
    "Luigi's Mansion",
    "Mario Kart",
    "Mario Party",
    "Fall Guys",
    "Little Hope",
    "Switch Sports",
    "Pokemon Unite",
]
board_games = [
    "Ticket to Ride",
    "Zombicide",
    "Homebrewers",
    "Masmora",
    "Pandemic",
    "Tea Dragons",
    "Dice Throne",
    "Scythe",
    "Wingspan",
    "Tiny Epic Pirates",
    "Eschaton",
    "Villainous",
    "Splendor",
    "Good Puppers",
]

def choose_game(choice):
    if choice in ["boardgame", "b"]:
        print(f"\nYou should play {random.choice(board_games)}")
    elif choice in ["videogame", "v"]:
        print(f"\nYou should play {random.choice(video_games)}")
    else:
        print("Please enter a valid choice.\n")

def choose_media(choice):
    if choice in ["movie", "m"]:
        print(f"\nYou should watch {random.choice(movies)}\n")
    elif choice in ["show", "s"]:
        print(f"\nYou should watch {random.choice(shows)}\n")
    else:
        print("Please enter a valid choice.\n")

def main():
    run = True

    while run:
        my_choice = str(input("\nWatch(w) or Play(p)? ")).lower()

        if my_choice in ["watch", "w"]:
            second_choice = str(input("\nMovie(m) or Show(s)? ")).lower()
            choose_media(second_choice)
            # break

        elif my_choice in ["play", "p"]:
            second_choice = str(input("\nBoardgame(b) or Videogame(v)? "))
            choose_game(second_choice)
            # break


if __name__ == '__main__':
    main()

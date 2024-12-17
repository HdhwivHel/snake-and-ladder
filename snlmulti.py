from random import *

def num_gen():
    dice = randrange(1,7)
    return dice

def intro():
    start = input("Press START to start the game: ")
    start.lower()

    if start == 'start' or start == 's':
        players = []

        n = int(input("Enter number of players: "))
        if n > 0:
            for i in range(n):
                name = input("Enter name: ")
                players.append({"name": name, "position":-1})
                name.upper()
                
            print(players)
            moving(players)

    else:
        print("Come again later")
        print()
        print()
        intro()


def moving(players):
    # ladder positions
    lad_dict = { 1:38, 
                            4: 14,
                            8 :30,
                            21 : 42,
                            28: 76,
                            50:67,
                            71:92,
                            80:99,
                }
                # snake positions
    sna_dict = { 32:10,
                            36: 6,
                            48 :26,
                            62 : 18,
                            88: 24,
                            95:56,
                            97:78,     
                }
    game_over = False
    
    
    while not game_over:
        for i in players:
            
            if i["position"] >= 0:
                pos = i["position"]
                diff = 100-pos
                if pos < 100:
                    print()
                    print(f"It is {i["name"]}\'s turn")
                    d = input("Enter `d` to roll dice: ")
                    d.lower()

                    if d == 'd':
                        dice = num_gen()
                        print(f"Dice: " ,dice)

                        if diff >= dice:
                            pos+=dice
                            i["position"] = pos
                            
                            # when you reach ladder
                            if pos in lad_dict:
                                print(f"You climbed a ladder!")
                                pos = lad_dict[pos]
                                i["position"] = pos

                            # when you reach snake
                            if pos in sna_dict:
                                print(f"Oops! You got bitten by a snake")
                                pos = sna_dict[pos]
                                i["position"] = pos

                            print(f"Current position: ",pos)
                            print()

                        else:
                            print(f"Current position: ",pos)
                            i["position"] = pos
                            print()
                        if pos == 100:
                            print(f"Congratulations {i["name"]}! You won!!")
                            game_over = True
                            exit()  
                            
                    else:
                        print()
                        print("Invalid Option!!")
                        exit()
                    
  
            else:
                print()
                print(f"It is {i["name"]}\'s turn")
                d = input("Enter `d` to roll dice. Roll a '6' to start the game: ")
                d.lower()
                if d == 'd':
                    dice = num_gen()
                    print(f"Dice: {dice}" )

                    if dice == 6:
                        pos = 0
                        print("You are now in the game ")
                        print()
                        print()
                        i["position"] = 0


def main():
    intro()
    
main()
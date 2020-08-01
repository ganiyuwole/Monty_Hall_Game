from time import sleep
import random

def user_door_pick():
    PICK_MEASSAGE = fr'For the price to win a car enter "door1" or "door2" or "door3" '
    door_values = [
        {"door1": "goat", "door2": "goat", "door3": "car"}
    ]
    PRIZE_DOOR = list(door_values[0].keys())[2]
    while True:
        user_name = input('Enter your name : ').title()
        if user_name.isdigit():
            print('Your name can not be a number, Enter a valid name')
        else:
            break
    dislay_meassage = len(PICK_MEASSAGE) + len(user_name)
    print(dislay_meassage * "=")
    user_pick_input = input(
        f"{user_name} {PICK_MEASSAGE} : ")
    for door in door_values:
        doors = list(door.keys())
        for d in doors:
            if user_pick_input == d:
                print(f'{user_name} the door you choose to open is {d}. ')
                break
    print('Now Monty Hall is picking a door please wait........')
    sleep(0.5)
    user_choice = door.pop(user_pick_input)
    swtich_prize = monty_door_pick(PRIZE_DOOR, door)
    swtich_door(user_pick_input, user_choice, user_name, swtich_prize)
 # This function allow monty hall to pick  a after user is done with picking his door


def monty_door_pick(PRIZE_DOOR, door):
    if PRIZE_DOOR in door:
        Switch_prize = door.pop(PRIZE_DOOR)
        monty_pick = random.choice(list(door))
        monty_choice = door.pop(monty_pick)
        door["door3"] = Switch_prize
        print(
            f'Monty Hall is now Opening ({monty_pick}) and we have a ({monty_choice}). ')
        sleep(0.5)
        return door
    elif PRIZE_DOOR not in door:
        monty_pick = random.choice(list(door))
        monty_choice = door.pop(monty_pick)
        print(
            f'Monty Hall is now Opening {monty_pick} and we have a {monty_choice}.')
        return door
 # The function allows user to switch door if they change their mind, else the winning door would be the first door user opened.


def swtich_door(user_frst_door, usr_frst_door_price, user_name, switch_prize):
    door_values = list(switch_prize.keys())[0]
    user_switch_door_input = input(
        f'{user_name} would you like to switch your door number? ({list(switch_prize.keys())[0]}) is the avaible choice, enter "y" for yes or "n" for no : ')
    if user_switch_door_input == 'y':
        print(
            f'{user_name} your first choice of ({user_frst_door}) revaling a ({usr_frst_door_price}) switched to your second door choice of ({door_values}) and revealing a ({switch_prize[door_values].capitalize()}) price. ')
    else:
        print(
            f'{user_name} your first door choice is ({user_frst_door}) and you won a ({usr_frst_door_price}) price. ')


def run_program():
    user_door_pick()


if __name__ == "__main__":
    run_program()

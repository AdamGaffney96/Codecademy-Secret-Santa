from random import choice, randint
from typing import List

# This function loads the names to pair from the local file.
def load_names(name_file: str) -> List[str]:
    with open(name_file, "r") as names:
        return [name.rstrip() for name in names]

# This function selects the second of the pair and then returns that pair as a list
def select_pair(name_list: List[str], not_yet_chosen: List[int], santa: str) -> List[str]:
    return [santa, name_list[choice(not_yet_chosen)]]

# This function recursively cycles through the provided list, and compiles a 2D list of pairings for secret santa
def santas_pairings(name_list: List[str], santa_index: int = 0, chosen: List[int] = [], pairings: List[str] = []) -> List[str]:
    if santa_index == len(name_list):
        return 0
    santa = name_list[santa_index]
    santas_choices = [num for num in range(0, len(name_list)) if num != name_list.index(santa) and num not in chosen]
    # I encountered a rare situation where the last person to pick would only have themselves to choose from. This checks if that has occured and swaps the name with a random person that has already been chosen.
    if len(santas_choices) == 0:
        swapping_index = randint(0, 10)
        swapped = pairings[swapping_index][1]
        pairings[swapping_index][1] = santa
        santas_choices.append(name_list.index(swapped))
    chosen_pairing = select_pair(name_list, santas_choices, santa)
    pairings.append(chosen_pairing)
    chosen.append(name_list.index(chosen_pairing[1]))
    # Recursive function call
    santas_pairings(name_list, santa_index + 1, chosen, pairings)
    return pairings

# This function recursively displays the pairings that have been chosen, with an option for a specific price limit
def display_santas_choices(pairing_list: List[str], index: int = 0, price_limit: int = 20) -> str:    
    if index == len(pairing_list):
        return "complete"
    current_pair = pairing_list[index]
    print(f"{current_pair[0]} will now be Santa for...{current_pair[1]}!")
    # Recursive function call
    display_santas_choices(pairing_list, index + 1)
    if index == 0:
        print(f"\nDon't forget about the ${price_limit} limit!")
    return "complete"

# The main function call
if __name__ == "__main__":
    print("It's that time of year again! Time to select the pairings for this years Secret Santa.\n")
    print("!! Don't let the participants see, otherwise Santa wouldn't be so secret would they?\n")
    name_list = load_names("names.txt")
    santa_pairings = santas_pairings(name_list)
    display_santas_choices(santa_pairings)
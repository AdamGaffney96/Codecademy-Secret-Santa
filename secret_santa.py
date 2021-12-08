from random import choice
from typing import List

def load_names(name_file: str) -> List[str]:
    with open(name_file, "r") as names:
        return [name.rstrip() for name in names]

def select_pair(name_list: List[str], not_yet_chosen: List[int], santa: str) -> List[str]:
    print(not_yet_chosen)
    return [santa, name_list[choice(not_yet_chosen)]]

def santas_pairings(name_list: List[str], santa_index: int = 0, chosen: List[int] = [], pairings: List[str] = []) -> List[str]:
    if santa_index == len(name_list):
        return 0
    santa = name_list[santa_index]
    santas_choices = [num for num in range(0, len(name_list)) if num != name_list.index(santa) and num not in chosen]
    chosen_pairing = select_pair(name_list, santas_choices, santa)
    pairings.append(chosen_pairing)
    chosen.append(name_list.index(chosen_pairing[1]))
    santas_pairings(name_list, santa_index + 1, chosen, pairings)
    return pairings

def display_santas_choices(pairing_list: List[str], index: int = 0, price_limit: int = 20) -> str:
    if index == len(pairing_list):
        return "complete"
    current_pair = pairing_list[index]
    print(f"{current_pair[0]} will now be Santa for...{current_pair[1]}!")
    display_santas_choices(pairing_list, index + 1)
    if index == 0:
        print(f"Don't forget about the ${price_limit} limit!")
    return "complete"

if __name__ == "__main__":
    name_list = load_names("names.txt")
    santa_pairings = santas_pairings(name_list)
    print(santa_pairings)
    display_santas_choices(santa_pairings)
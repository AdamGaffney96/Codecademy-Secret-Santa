from function_defs import load_names, santas_pairings, display_santas_choices

# The main function call
if __name__ == "__main__":
    print("It's that time of year again! Time to select the pairings for this years Secret Santa.\n")
    print("!! Don't let the participants see, otherwise Santa wouldn't be so secret would they?\n")
    name_list = load_names("names.txt")
    santa_pairings = santas_pairings(name_list)
    display_santas_choices(santa_pairings)
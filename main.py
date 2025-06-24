import json



def load_data():
    with open("json/champions.json", "r") as f:
        champions = json.load(f)
    with open("json/traits.json", "r") as f:
        traits = json.load(f)
    return champions, traits


#find a composition with the maximum amount of emblems used for traits, where it is not redundant (like syndicate 6)

def evaluate_traits(team, emblems, traits):
    return 0

#it should be in order of 
# 1. the amount of emblems used
# 2. the amount of traits active
# 3. the sum of the champions' costs

#filter the list of compositions with the champions used


#filter the list of compositions with the team_size












team_size = 9
emblems = ["Techie", "Vanguard", "Street Demon", "Golden Ox", "Slayer"]
champions = ["Brand", "Jarvan"]
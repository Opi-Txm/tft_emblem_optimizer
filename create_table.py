import itertools
import json
import composition_pb2  # generated from .proto
from pathlib import Path
from collections import Counter


def load_data():
    with open("json/champions.json") as f:
        champions_raw = json.load(f)
    return [(champions["id"], champions["traits"]) for champions in champions_raw]

def simulate_combinations(team_size: int, champions: list[tuple[int, list[int]]]) :
    res = []

    for composition in itertools.combinations(champions, team_size):
        champ_ids = [champ[0] for champ in composition]
        team_traits = []

        for _, champ_traits in composition:
            team_traits.extend(champ_traits)

        trait_counts = Counter(team_traits)
        trait_tuples = [(trait_id, count) for trait_id, count in trait_counts.items()]

        res.append([champ_ids, trait_tuples])
        
    return res


def main():
    team_size = int(input("Enter team size: "))
    champions = load_data()
    list_comps = simulate_combinations(team_size, champions)

    with open("list", "w") as f:
        json.dump(list_comps, f, indent=2)

if __name__ == "__main__":
    main()

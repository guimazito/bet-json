import pandas as pd
from common import (
    read_file
)


def megasena1(my_list: list):
    """
    Generate a Mega-Sena simple game and compare with all previous Mega-Sena games
    """
    result = read_file(f"db\\megasena_database")

    print(f"\nMy game: {my_list}")

    for i in result:
        print(f"\nComparing...")
        lst = [i["n1"], i["n2"], i["n3"], i["n4"], i["n5"], i["n6"]]
        if my_list == lst:
            print(f"My Game: {my_list}\nGame {i["game"]}: {lst}\nSame!")
            break
        else:
            print(f"My Game: {my_list}\nGame {i["game"]}: {lst}\nDifferent")

def lotofacil1(my_list: list):
    """
    Receive 15 numbers from user and check the probability in database comparing with previous games
    """
    file = read_file(f"db\\lotofacil_database")

    print(f"\nMy game: {my_list}")

    result = []

    for i in file:

        numbers = [i["n1"], i["n2"], i["n3"], i["n4"], i["n5"], i["n6"], i["n7"], i["n8"], i["n9"], i["n10"], i["n11"], i["n12"], i["n13"], i["n14"], i["n15"]]

        intersection = set(my_list).intersection(numbers)
        result.append(
            {
                "game": i["game"],
                "numbers": numbers,
                "result": len(intersection)
            }
        )

    df = pd.DataFrame.from_dict(result)
    df = df.set_index("game")
    pd.set_option("display.max_rows", None)
    df = df.sort_values(by=["result"], ascending=False)
    df = df.head(200)

    print(df)
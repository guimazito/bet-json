from api import (
    get_data,
    get_quantity
)
from common import (
    sleep,
    read_file,
    save_file,
    convert_str2int,
    convert_datetime
)

def update_game_database(game_type: str):

    result = read_file(f"db\\{game_type}_database")

    database_quantity = len(result)
    online_quantity = get_quantity(game_type)

    print("\nChecking Status...")
    print(f"Database: {database_quantity} games")
    print(f"Loterias.Caixa: {online_quantity} games")

    if database_quantity != online_quantity:

        print(f"\nYou're {int(online_quantity)-int(database_quantity)} games behind!")
        print("\nUpdating your database...")

        for i in range(database_quantity + 1, online_quantity + 1):

            game = False
            
            # Checking if game is already saved on json
            for j in result:
                if j["game"] == i:                        
                    game = True

            if not game:

                print(f"\nGetting game {i} ...")
                response = get_data(game_type, i)

                n = convert_str2int(response["listaDezenas"])

                if game_type == "megasena":

                    result.append(
                        {
                            "game": response["numero"],
                            "date": convert_datetime(response["dataApuracao"]),
                            "n1": n[0],
                            "n2": n[1],
                            "n3": n[2],
                            "n4": n[3],
                            "n5": n[4],
                            "n6": n[5]
                        }
                    )

                elif game_type == "lotofacil":

                    result.append(
                        {
                            "game": response["numero"],
                            "date": convert_datetime(response["dataApuracao"]),
                            "n1": n[0],
                            "n2": n[1],
                            "n3": n[2],
                            "n4": n[3],
                            "n5": n[4],
                            "n6": n[5],
                            "n7": n[6],
                            "n8": n[7],
                            "n9": n[8],
                            "n10": n[9],
                            "n11": n[10],
                            "n12": n[11],
                            "n13": n[12],
                            "n14": n[13],
                            "n15": n[14]
                        }
                    )

                sleep(5)

            else:
                print(f"\nGame {i} already saved on database!")

        save_file(f"db\\{game_type}_database", result)
        print("\nSaved on database!")

    else:
        print(f"\nYour database is updated!")

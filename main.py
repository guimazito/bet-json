import sys
from data_mining import (
    update_game_database
)
from common import (
    create_file,
    convert_str2int,
    generate_random_list
)
from strategy import (
    megasena1,
    lotofacil1
)

menu = "\n -------------------------------------MENU------------------------------------\
        \n| 1. Generate a Mega-Sena Simple Game                                         |\
        \n| 2. Generate a Lotofacil Simple Game                                         |\
        \n|-----------------------------------------------------------------------------|\
        \n| 3. Update your Mega-Sena Database                                           |\
        \n| 4. Update your Lotofacil Database                                           |\
        \n|-----------------------------------------------------------------------------|\
        \n| 5. Generate a Mega-Sena Game and Compare with Previous Games                |\
        \n| 6. Check the Probability of your Lotofacil Game with Previous Games         |\
        \n|-----------------------------------------------------------------------------|\
        \n| 7. Create Excel File from Lotofacil Games                                   |\
        \n| 0. Exit                                                                     |\
        \n -----------------------------------------------------------------------------\
        \nOption: "

while True:

    option = input(menu)

    match option:

        case "1":
            generate_random_list("megasena")

        case "2":
            generate_random_list("lotofacil")

        case "3":
            update_game_database("megasena")

        case "4":
            update_game_database("lotofacil")
        
        case "5":
            my_list = generate_random_list("megasena")
            megasena1(my_list)

        case "6":
            my_list = input("\nEnter your 15 Numbers (Ex: 1,3,5,7...): ")
            my_list = my_list.replace(" ", "")
            my_list = my_list.split(',')
            lotofacil1(convert_str2int(my_list))

        case "7":
            create_file()

        case "0":
            print("\nBye Bye...\n")
            sys.exit(0)

        case _:
            print("\nInvalid Option!\n")

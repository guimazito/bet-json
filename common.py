import re
import time
import json
import random
import xlwings as xw
from datetime import datetime


def generate_random_list(game_type: str):
  match game_type:

    case "megasena":
        result = random.sample(range(1, 61), 6)
        result.sort()
        print(f"\n{result}")
        return result

    case "lotofacil":
        result = random.sample(range(1, 26), 15)
        result.sort()
        print(f"\n{result}")
        return result
     
    case _:
        print('Wrong Game Type!')

def remove_leading_zeros(number: str):
    # Regex to remove leading zeros from a string  
    regex = "^0+(?!$)"
    # Replaces the matched value with given string
    return re.sub(regex, "", number)

def convert_str2int(lst: list):
   return [eval(remove_leading_zeros(i)) for i in lst]

def convert_datetime(date: str):
    return datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")

def sleep(seconds: int):
    time.sleep(seconds)

def save_file(file_name: str, result: dict):
    json_object = json.dumps(result)
    with open(f"{file_name}.json", "w") as file:
        file.write(json_object)

def read_file(file_name: str):
   with open(f"{file_name}.json", "r") as file:
    return json.load(file)

def create_file():
    print("\nReading database...")

    result = read_file(f"db\\lotofacil_database")
    
    with xw.App(visible=False) as app:
        print("Saving file...")
        wb = xw.Book()
        ws = wb.sheets(1)

        ws.range("A1").value = "game"
        ws.range("B1").value = "n1"
        ws.range("C1").value = "n2"
        ws.range("D1").value = "n3"
        ws.range("E1").value = "n4"
        ws.range("F1").value = "n5"
        ws.range("G1").value = "n6"
        ws.range("H1").value = "n7"
        ws.range("I1").value = "n8"
        ws.range("J1").value = "n9"
        ws.range("K1").value = "n10"
        ws.range("L1").value = "n11"
        ws.range("M1").value = "n12"
        ws.range("N1").value = "n13"
        ws.range("O1").value = "n14"
        ws.range("P1").value = "n15"
        ws.range("Q1").value = "n16"
        ws.range("R1").value = "n17"
        ws.range("S1").value = "n18"
        ws.range("T1").value = "n19"
        ws.range("U1").value = "n20"
        ws.range("V1").value = "n21"
        ws.range("W1").value = "n22"
        ws.range("X1").value = "n23"
        ws.range("Y1").value = "n24"
        ws.range("Z1").value = "n25"

        r = 2
        color = "#c6efce"
        font_color = "#006100"

        for i in result:
            numbers = [i["n1"], i["n2"], i["n3"], i["n4"], i["n5"], i["n6"], i["n7"], i["n8"], i["n9"], i["n10"], i["n11"], i["n12"], i["n13"], i["n14"], i["n15"]]
            
            ws.range(f"A{r}").value = i["game"]
            
            ws.range(f"B{r}").value = 1
            if 1 in numbers:
                ws.range(f"B{r}").color = color
                ws.range(f"B{r}").font.color = font_color

            ws.range(f"C{r}").value = 2
            if 2 in numbers:
                ws.range(f"C{r}").color = color
                ws.range(f"C{r}").font.color = font_color

            ws.range(f"D{r}").value = 3
            if 3 in numbers:
                ws.range(f"D{r}").color = color
                ws.range(f"D{r}").font.color = font_color

            ws.range(f"E{r}").value = 4
            if 4 in numbers:
                ws.range(f"E{r}").color = color
                ws.range(f"E{r}").font.color = font_color

            ws.range(f"F{r}").value = 5
            if 5 in numbers:
                ws.range(f"F{r}").color = color
                ws.range(f"F{r}").font.color = font_color

            ws.range(f"G{r}").value = 6
            if 6 in numbers:
                ws.range(f"G{r}").color = color
                ws.range(f"G{r}").font.color = font_color

            ws.range(f"H{r}").value = 7
            if 7 in numbers:
                ws.range(f"H{r}").color = color
                ws.range(f"H{r}").font.color = font_color

            ws.range(f"I{r}").value = 8
            if 8 in numbers:
                ws.range(f"I{r}").color = color
                ws.range(f"I{r}").font.color = font_color

            ws.range(f"J{r}").value = 9
            if 9 in numbers:
                ws.range(f"J{r}").color = color
                ws.range(f"J{r}").font.color = font_color

            ws.range(f"K{r}").value = 10
            if 10 in numbers:
                ws.range(f"K{r}").color = color
                ws.range(f"K{r}").font.color = font_color

            ws.range(f"L{r}").value = 11
            if 11 in numbers:
                ws.range(f"L{r}").color = color
                ws.range(f"L{r}").font.color = font_color

            ws.range(f"M{r}").value = 12
            if 12 in numbers:
                ws.range(f"M{r}").color = color
                ws.range(f"M{r}").font.color = font_color

            ws.range(f"N{r}").value = 13
            if 13 in numbers:
                ws.range(f"N{r}").color = color
                ws.range(f"N{r}").font.color = font_color

            ws.range(f"O{r}").value = 14
            if 14 in numbers:
                ws.range(f"O{r}").color = color
                ws.range(f"O{r}").font.color = font_color

            ws.range(f"P{r}").value = 15
            if 15 in numbers:
                ws.range(f"P{r}").color = color
                ws.range(f"P{r}").font.color = font_color

            ws.range(f"Q{r}").value = 16
            if 16 in numbers:
                ws.range(f"Q{r}").color = color
                ws.range(f"Q{r}").font.color = font_color

            ws.range(f"R{r}").value = 17
            if 17 in numbers:
                ws.range(f"R{r}").color = color
                ws.range(f"R{r}").font.color = font_color

            ws.range(f"S{r}").value = 18
            if 18 in numbers:
                ws.range(f"S{r}").color = color
                ws.range(f"S{r}").font.color = font_color

            ws.range(f"T{r}").value = 19
            if 19 in numbers:
                ws.range(f"T{r}").color = color
                ws.range(f"T{r}").font.color = font_color

            ws.range(f"U{r}").value = 20
            if 20 in numbers:
                ws.range(f"U{r}").color = color
                ws.range(f"U{r}").font.color = font_color

            ws.range(f"V{r}").value = 21
            if 21 in numbers:
                ws.range(f"V{r}").color = color
                ws.range(f"V{r}").font.color = font_color

            ws.range(f"W{r}").value = 22
            if 22 in numbers:
                ws.range(f"W{r}").color = color
                ws.range(f"W{r}").font.color = font_color

            ws.range(f"X{r}").value = 23
            if 23 in numbers:
                ws.range(f"X{r}").color = color
                ws.range(f"X{r}").font.color = font_color

            ws.range(f"Y{r}").value = 24
            if 24 in numbers:
                ws.range(f"Y{r}").color = color
                ws.range(f"Y{r}").font.color = font_color

            ws.range(f"Z{r}").value = 25
            if 25 in numbers:
                ws.range(f"Z{r}").color = color
                ws.range(f"Z{r}").font.color = font_color

            r += 1

        wb.save("export\\lotofacil_games.xlsx")
        wb.close()
        print("Saved!")

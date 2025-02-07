#-*- coding: utf-8 -*-
import google.generativeai as genai
import random
import os
import re
from time import sleep

# Tömmer skärmen på innehåll
clear = lambda: os.system('cls')

# Ange ordet som ska användas för spelet. Kör en clear så inte spelaren kan se ordet.
Word = input("Enter a word to use for the game: ")
clear()


# Samtliga olika utseenden på den hängande gubben...
row0= ""
row7_1 = "HANGMAN"
row6_1 = "   ____"
row5_1 = "  |"
row5_2 = "  |/"
row5_3 = "  |/   |"
row4_1 = "  |"
row4_2 = "  |    O"
row3_1 = "  |"
row3_2 = "  |    |"
row3_3 = "  |   /|"
row3_4 = "  |   /|\\"
row2_1 = " / \\"
row2_2 = " / \\  /"
row2_3 = " / \\  / \\"
row1_1 = "/   \\"


# Dom olika kombinationerna som gubben kan ha.
Shoot0=f""" {row7_1}
{row0}
{row0}
{row0}
{row0}
{row0}
{row0}
"""

Shoot1=f""" {row7_1}
{row0}
{row0}
{row0}
{row0}
{row2_1}
{row1_1}
"""

Shoot2=f""" {row7_1}
{row0}
{row5_1}
{row4_1}
{row3_1}
{row2_1}
{row1_1}
"""

Shoot3=f""" {row7_1}
{row6_1}
{row5_1}
{row4_1}
{row3_1}
{row2_1}
{row1_1}
"""

Shoot4=f""" {row7_1}
{row6_1}
{row5_2}
{row4_1}
{row3_1}
{row2_1}
{row1_1}
"""

Shoot5=f""" {row7_1}
{row6_1}
{row5_3}
{row4_1}
{row3_1}
{row2_1}
{row1_1}
"""

Shoot6=f""" {row7_1}
{row6_1}
{row5_3}
{row4_2}
{row3_1}
{row2_1}
{row1_1}
"""

Shoot7=f""" {row7_1}
{row6_1}
{row5_3}
{row4_2}
{row3_2}
{row2_1}
{row1_1}
"""

Shoot8=f""" {row7_1}
{row6_1}
{row5_3}
{row4_2}
{row3_3}
{row2_1}
{row1_1}
"""

Shoot9=f""" {row7_1}
{row6_1}
{row5_3}
{row4_2}
{row3_4}
{row2_1}
{row1_1}
"""

Shoot10=f""" {row7_1}
{row6_1}
{row5_3}
{row4_2}
{row3_4}
{row2_2}
{row1_1}
"""

Shoot11=f""" {row7_1}
{row6_1}
{row5_3}
{row4_2}
{row3_4}
{row2_3}
{row1_1}
GAME OVER"""

# Konverterar ordet till streck och slänger in dom träffade bokstäverna.
def ConvertLine(UsedChar, Word):
    CharLeft = 0
    HiddenName = ""
    i = 0
    while i < len(Word):
        if Word[i].lower() in UsedChar.lower():
            HiddenName = HiddenName + Word[i] + " "
        else:
            HiddenName = HiddenName + "_ "
            CharLeft += 1
        i += 1
    return(HiddenName, CharLeft)

# Funktionen som ber ai gissa en bokstav.
def guess(status, used):
    #Some settings for ai.
    genai.configure(api_key="din api key")
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 20000,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )
    chat_session = model.start_chat(
        history=[
        ]
    )
    response = model.generate_content(
        f"Du ska spela hänga gubbe på dessa streck/bokstäver: {status}\nDu har tidigare sagt: {used}\nSäg en bokstav som du tror saknas. Validera att bokstaven du tänker säga i kombination med dom andra bokstäverna i {status} skapar ett riktigt ord. Enbart en bokstav inget annat!"
    )
    return(response.text)

#Sätter variablarna tomma vid starten.
UsedChar = ""
tries = 0

# Spelfunktionen
while True:
    # Skapar den streckade ersättningen för ordet.
    HiddenName, CharLeft = ConvertLine(UsedChar, Word)

    # Skapar variabelnamnet som innehåller gubben.
    variable_name="Shoot" + str(tries)

    # Tömmer skärmen och skriver ut gubben och vilka ord den träffat.
    clear()
    print(globals()[variable_name])
    print(HiddenName)
    print(f"Used char: {UsedChar}")
    print("")
    # Kollar om ordet är löst
    if not CharLeft == 0:
        if not tries == 11:
            #Ber ai gissa en bokstav.
            sleep(3)
            x = str(guess(HiddenName, UsedChar)).replace(" ", "").replace("\n", "").lower()

            #x = input("Enter a Char: ")
            # Kollar om användaren lyckades med att skriva en bokstav.
        
            if len(x) == 1:
                # Kollar om det är första gissningen eller inte.
                if UsedChar == "":
                    UsedChar = x
                else:

                    # Kollar att bokstaven inte tidigare har blivit körd.
                    if not x in UsedChar:
                        UsedChar = UsedChar + "," + x
                
                # Verifierar om bokstaven finns med i ordet. Och gör den inte det så hängs gubben lite till.
                if not x in Word:
                    tries += 1
                
                # Max antal försök. Kummer du hit är du gameover.
        else:
            print(f"The word was: {Word}")
            break
    else:
        # Ordet är löst
        print("YOU SOLVED IT!")      
        break  


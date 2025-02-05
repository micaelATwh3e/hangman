import random
import os
import re

# Tömmer skärmen på innehåll
clear = lambda: os.system('cls')

# Ord som ska finnas i spelet.
a = ["började", "använda", "behöver", "finns", "mellan", "genom", "eftersom", "därför", "alltid", "aldrig", "också", "vanligt", "viktigt", "roligt", "intressant", "svårt", "lätt", "stort", "litet", "gammalt", "ungt", "vackert", "fult", "snabbt", "långsamt", "högt", "lågt", "varmt", "kallt", "sött", "surt", "salt", "beskt", "mjukt", "hårt", "viktigt", "onödigt", "intressant", "tråkigt", "lätt", "svårt", "roligt", "allvarligt", "vänligt", "ovänligt", "snällt", "elakt", "dumt", "smart", "klokt", "vist", "galet", "lyckligt", "ledset", "argt", "rädd", "trött", "piggt", "hungrigt", "mätt", "törstigt", "fullt", "tomt", "helt", "trasigt", "rent", "smutsigt", "ljust", "mörkt", "tyst", "högljutt", "vilt", "tam", "fritt", "bundet", "rikt", "fattigt", "känt", "okänt", "viktigt", "oviktigt", "försöka", "förstå", "hjälpa", "behöva", "kunna", "vilja", "måste", "skulle", "borde", "verkligen", "faktiskt", "tyvärr", "antagligen", "förmodligen", "dessutom", "istället", "fortfarande", "tillsammans", "ensam", "själv", "andra", "olika", "samma", "egna", "vissa", "flesta", "båda", "ingen", "någon", "mycket", "lite", "mer", "mindre", "mest", "minst"]

# Väljer ett random ord
Word = random.choice(a)

# Samtliga olika utseenden på den hängande gubben...
row0= ""
row7_1 = "HANGMAN (100 most common swedish words.. If you ask Gemini)"
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
            x = input("Enter a Char: ")
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


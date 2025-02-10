import tkinter as tk
import random

# List with words to play with.
a = ["började", "använda", "behöver", "finns", "mellan", "genom", "eftersom", "därför", "alltid", "aldrig", "också", "vanligt", "viktigt", "roligt", "intressant", "svårt", "lätt", "stort", "litet", "gammalt", "ungt", "vackert", "fult", "snabbt", "långsamt", "högt", "lågt", "varmt", "kallt", "sött", "surt", "salt", "beskt", "mjukt", "hårt", "viktigt", "onödigt", "intressant", "tråkigt", "lätt", "svårt", "roligt", "allvarligt", "vänligt", "ovänligt", "snällt", "elakt", "dumt", "smart", "klokt", "vist", "galet", "lyckligt", "ledset", "argt", "rädd", "trött", "piggt", "hungrigt", "mätt", "törstigt", "fullt", "tomt", "helt", "trasigt", "rent", "smutsigt", "ljust", "mörkt", "tyst", "högljutt", "vilt", "tam", "fritt", "bundet", "rikt", "fattigt", "känt", "okänt", "viktigt", "oviktigt", "försöka", "förstå", "hjälpa", "behöva", "kunna", "vilja", "måste", "skulle", "borde", "verkligen", "faktiskt", "tyvärr", "antagligen", "förmodligen", "dessutom", "istället", "fortfarande", "tillsammans", "ensam", "själv", "andra", "olika", "samma", "egna", "vissa", "flesta", "båda", "ingen", "någon", "mycket", "lite", "mer", "mindre", "mest", "minst"]
Word = random.choice(a)

UsedCharVar = ""

# Constants for the hangman design
row0= ""
row7_1 = "HANGMAN"
row6_1 = "   ____"
row5_1 = "  |"
row5_2 = "  |/"
row5_3 = "  |/  |"
row4_1 = "  |"
row4_2 = "  |   O"
row3_1 = "  |"
row3_2 = "  |   |"
row3_3 = "  |  /|"
row3_4 = "  |  /|\\"
row2_1 = " / \\"
row2_2 = " / \\ /"
row2_3 = " / \\ / \\"
row1_1 = "/   \\"


# Tkinter gui
root = tk.Tk()
root.title("Hangman")
root.geometry("400x400")

#the hangman design
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

# Resetting the game
tries = 0

# Function to convert the word to a hidden word
def ConvertLine(UsedCharVar, Word):
    CharLeft = 0
    HiddenName = ""
    i = 0
    while i < len(Word):
        if Word[i].lower() in UsedCharVar.lower():
            HiddenName = HiddenName + Word[i] + " "
        else:
            HiddenName = HiddenName + "_ "
            CharLeft += 1
        i += 1
    return(HiddenName, CharLeft)


# Showing the hangman design
variable_name="Shoot" + str(tries)
Gubben = tk.Label(root, text=globals()[variable_name], font=("Terminal", 14), justify="left")
Gubben.pack(pady=5)

# The Word in format: _ _ _ _ _
HiddenName, CharLeft = ConvertLine(UsedCharVar, Word)
UsedWord = tk.Label(root, text=HiddenName, font=("Arial", 12))
UsedWord.pack(pady=5)


# The used characters
UsedChar = tk.Label(root, text="Used char:\n", font=("Arial", 12))
UsedChar.pack(pady=5)

# Input label
InputLabel = tk.Label(root, text="Enter char:", font=("Arial", 12))
InputLabel.pack(pady=5)

# Entry box, for guessing char
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Resetting the game
def reset_game():
    global UsedCharVar, tries, variable_name, Shoot0, Shoot1, Shoot2, Shoot3, Shoot4, Shoot5, Shoot6, Shoot7, Shoot8, Shoot9, Shoot10, Shoot11, CharLeft, Word
    Word = random.choice(a)
    tries = 0
    UsedCharVar=""
    variable_name="Shoot" + str(tries)
    Gubben.config(text=globals()[variable_name])
    HiddenName, CharLeft = ConvertLine(UsedCharVar, Word)
    UsedWord.config(text=HiddenName)
    UsedChar.config(text="Used char:\n" + UsedCharVar)
    send_button.config(text= "Send")


def send_message():  # No argument needed
    if send_button['text'] == "Reset":
        reset_game()
        return
    if len(entry.get()) != 1:
        return  
    # Access the global variable
    global UsedCharVar, tries, variable_name, Shoot0, Shoot1, Shoot2, Shoot3, Shoot4, Shoot5, Shoot6, Shoot7, Shoot8, Shoot9, Shoot10, Shoot11, CharLeft, Word
    new_text = entry.get()
    if UsedCharVar: # Check if UsedCharVar is not empty
        UsedCharVar += " " + new_text
    else:
        UsedCharVar = new_text
    UsedChar.config(text="Used char:\n" + UsedCharVar)
    entry.delete(0, tk.END) # Clear the entry box after sending

    # Vertifying of char is in word.. and show the hangman design.
    if not new_text in Word:
        tries += 1
        variable_name="Shoot" + str(tries)
    Gubben.config(text=globals()[variable_name])
    HiddenName, CharLeft = ConvertLine(UsedCharVar, Word)
    UsedWord.config(text=HiddenName)

    # Checking if the word is solved.
    if CharLeft == 0:
        Gubben.config(text="YOU SOLVED IT!\n\n\n\n\n\n\n")
        send_button.config(text= "Reset")

    # Checking if the user are game over.
    if  tries == 11:
        send_button.config(text= "Reset")
     


# Send button
send_button = tk.Button(root, text="Send", command=send_message)   
send_button.pack(pady=5)
print(Word)


root.mainloop()

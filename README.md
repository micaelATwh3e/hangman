# Inlämningsuppgifter till pyhtonkursen (hänga gubbe).

Starta programet genom python hangman.py

Spelet kommer välja ett av 100st förbereda ord från ordlistan i spelet. Du ska skriva en bokstav i taget som du tror finns i det ordet. Finns det inte med i order kommer gubben att hängas ett till steg. Svarar du en bokstav som finns i order kommer denna att visas på den stäckade raden. Man har 11 misslyckade försök på sig att gissa ordet.

tips kan vara att börja med att skriva vokalet som inte är så många och garanterat finns i orden. Sen när man har någon/några träffas kan man skriva andra bokstäver som oftas fungerar i kombination med vokalen. och vips så har du gissat ordet.


4st branches.

main  - innehåller ett hänhga gubbe där ordet välj från en ordlista. 100 ord i listan.

extra_future - Samma som main men man får som användare ange ett ord åt spelaren.

ai - samma som extra_future, men det är gemini som spelar spelet. Kräver en api nyckel.

gui - Addade en hänga gubbe i tkinter också. samma function som main.

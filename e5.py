"""
Ion Zarija, José Villalba, Omar Vargas
06/11/2023
ASIXc M03 UF1 A3 PR3
isBigger.py
"""

date = input().split('/')
year = int(date[2])
month = int(date[1])
day = int(date[0])
dateCorrect = (1 <= month <=12 and 1<= day <= 31)
bisiesto = False
if dateCorrect:
    if date[1] == 2:
        if year%4 == 0 and year%100 != 0 or year%400 == 0:
            bisiesto = True
        if day > 29 and bisiesto == True:
            print("No es vàlido")
    if day > 28 and bisiesto == False:
        print("No es valido")
else:
    print("No es valid")










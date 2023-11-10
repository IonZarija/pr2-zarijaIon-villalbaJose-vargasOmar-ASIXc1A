"""
Ion Zarija, José Villalba, Omar Vargas
06/11/2023
ASIXc M03 UF1 A3 PR3
isACorrectDate.py
Programa que comprovi si una data és correcte. El programa ha de demanar una data, dia, mes i any (en el format DD/MM/AAAA).
"""
try:
    date = input().split('/')
    year = int(date[2])
    month = int(date[1])
    day = int(date[0])
    dateCorrect = (1 <= month <= 12 and 1 <= day <= 31)
    if dateCorrect:
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day > 29:
                    print("No es vàlido")
                else:
                    print("Es valido")
            elif day > 28:
                print("No es valido")
            else:
                print("Es valido")
        else:
            match month:
                case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                    print("Es valido")
                case 4 | 6 | 9 | 11:
                    if day > 30:
                        print("No es valido")
                    else:
                        print("Es valido")
    else:
        print("No es valid")
except ValueError:
    print("Data no valida")










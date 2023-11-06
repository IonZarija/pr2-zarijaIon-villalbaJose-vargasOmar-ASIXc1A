"""
Ion Zarija, José Villalba, Omar Vargas
06/11/2023
ASIXc M03 UF1 A3 PR3
areGrowingNumbers.py
"""
num1 = int(input("Numero 1?: "))
num2 = int(input("Numero 2?: "))
num3 = int(input("Numero 3?: "))

if num1 <= num2 <= num3 and num1 <= num3:
    print("Orden creciente")

else:
    print("No orden creciente")

"""
Ion Zarija, José Villalba, Omar Vargas
06/11/2023
ASIXc M03 UF1 A3 PR3
isBigger.py
Programa que demana dos números si el primer és més gran o igual que el segon els intercanvia.
"""
num1 = int(input("Numero 1?: "))
num2 = int(input("Numero 2?: "))
v1 = 0
v2 = 0
if num2 >= num1:
    v1 = num2
    v2 = num1
else:
    v1 = num1
    v2 = num2
print(v1, v2)
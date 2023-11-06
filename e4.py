"""
Ion Zarija, José Villalba, Omar Vargas
06/11/2023
ASIXc M03 UF1 A3 PR3
customerLoyaltyCard.py
"""
baseimp = float(input("Introduce el importe base: "))
ptotal = 0
if baseimp >= 100:
    ptotal = baseimp*0.79
else:
    ptotal = baseimp

print("El importe es de: ", ptotal*1.21)


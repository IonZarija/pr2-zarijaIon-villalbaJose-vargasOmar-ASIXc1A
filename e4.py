"""
Ion Zarija, José Villalba, Omar Vargas
06/11/2023
ASIXc M03 UF1 A3 PR3
customerLoyaltyCard.py
"""

try:
    baseimp = float(input("Introduce el importe base: "))
except:
    print("STRING FAILURE")
    tarjeta = str(input("El usuario tiene en su pertenencia tarjeta?: "))
    ptotal = 0
    match tarjeta:
        case "si":
            if baseimp >= 100:
                ptotal = baseimp * 0.79
            else:
                ptotal = baseimp
            print("El importe es de: ", ptotal * 1.21)
        case _:
            print("El usuario no tiene descuento")





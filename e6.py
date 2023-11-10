"""
Ion Zarija, José Villalba, Omar Vargas
06/11/2023
ASIXc M03 UF1 A3 PR3
calculateMyWaterBill.py
L'usuari introdueix la lletra del tipus d'habitatge i número de m3  d'aigua gastats. Mostrar per pantalla el preu total de la factura de l’aigua.
"""
try:
    tipusHab = str(input("Tipus d'habitatge?: "))
    match tipusHab:
        case "A": quota = 2.46
        case "B": quota = 6.40
        case "C": quota = 7.25
        case "D": quota = 11.21
        case "E": quota = 12.10
        case "F": quota = 17.28
        case "G": quota = 28.01
        case "H": quota = 40.50
        case "I": quota = 61.31
    consum = int(input("Consum d'aigua en m³?: "))
    if 0 <= consum <= 6:
        preuCon = consum * 0.5849
    if 7 <= consum <= 9:
        preuCon = consum * 1.1699
    if 10 <= consum <= 15:
        preuCon = consum * 1.7548
    if 16 <= consum <= 18:
        preuCon = consum * 2.3397
    if consum > 18:
        preuCon = consum * 2.9246

    preuTotal = preuCon + quota
    print (f"El preu total és {preuTotal:.2f} ")
except ValueError:
    print("No es valid")
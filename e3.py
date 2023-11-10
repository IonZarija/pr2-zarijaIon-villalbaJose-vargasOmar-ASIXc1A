"""
Ion Zarija, José Villalba, Omar Vargas
06/11/2023
ASIXc M03 UF1 A3 PR3
fastAndFurious.py
Programa que calculi la velocitat instantània i la velocitat mitjana.
"""

velIni = int(input("Velocitat Inicial?: "))
acc = int(input("Acceleració?: "))
temps = int(input("Temps?: "))

velIns = velIni + acc * temps

if velIns <= 0:
    print("Està parat i no es pot calcular la velocitat mitjana")
else:
    velMitj = (velIns + velIni)/2
    print (f"La velocitat mitjana és {velMitj}")
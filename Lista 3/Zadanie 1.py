# -------------------------------Zadanie 1-----------------------------------
#Napisz program, który sprawdzi czy podana litera alfabetu jest samogloska czy spólgloska.
#Qt do
samogloski=['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y']

let=input('Wprowadz litere: ').lower()

if let in samogloski:
    print('Litera {} jest samogloska'.format(let))
else:
    print('{} jest spolgloska'.format(let))


